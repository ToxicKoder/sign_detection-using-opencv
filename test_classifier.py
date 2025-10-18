import cv2
import mediapipe as mp
import pickle
import numpy as np

# Load trained model
model_dict = pickle.load(open(r'D:\OPEN_CV\model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {0: 'A', 1: 'B', 2: 'L'}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # Extract all landmark coordinates
            data_aux = []
            x_ = []
            y_ = []

            for lm in hand_landmarks.landmark:
                x = lm.x
                y = lm.y
                data_aux.extend([x, y])
                x_.append(x)
                y_.append(y)

            # Predict once — AFTER collecting all landmark coordinates
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]

            # Get bounding box coordinates
            h, w, _ = frame.shape
            x1 = int(min(x_) * w) - 10
            y1 = int(min(y_) * h) - 10
            x2 = int(max(x_) * w) + 10
            y2 = int(max(y_) * h) + 10

            # Draw rectangle & text
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

            print(predicted_character)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):  # Press SPACE to quit
        break

cap.release()
cv2.destroyAllWindows()
