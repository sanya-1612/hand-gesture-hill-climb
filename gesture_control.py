import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    fingers = 0
    action = "IDLE"

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]
        landmarks = handLms.landmark

        tips = [4, 8, 12, 16, 20]

        # Thumb
        if landmarks[4].x < landmarks[3].x:
            fingers += 1

        # Other fingers
        for tip in tips[1:]:
            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers += 1

        if fingers == 5:
            action = "ACCELERATE"
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')

        elif fingers <= 1:
            action = "BRAKE"
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

        else:
            pyautogui.keyUp('right')
            pyautogui.keyUp('left')

        mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    else:
        pyautogui.keyUp('right')
        pyautogui.keyUp('left')
        action = "NO HAND"

    cv2.putText(img, f'Action: {action}', (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Hand Gesture Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
pyautogui.keyUp('right')
pyautogui.keyUp('left')
cv2.destroyAllWindows()
