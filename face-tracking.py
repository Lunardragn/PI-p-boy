import cv2
import sys
import time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

def get_eye_landmarks(face_landmarks):
    left_eye_landmarks = []
    right_eye_landmarks = []

    # Left eye landmarks indices
    left_eye_indices = list(range(133, 143))

    # Right eye landmarks indices
    right_eye_indices = list(range(362, 374))

    for idx in left_eye_indices:
        left_eye_landmarks.append(face_landmarks.landmark[idx])

    for idx in right_eye_indices:
        right_eye_landmarks.append(face_landmarks.landmark[idx])

    return left_eye_landmarks, right_eye_landmarks

def get_face_mesh(image):
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.multi_face_landmarks:
        return image

    annotated_image = image.copy()
    for face_landmarks in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image=annotated_image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)

        left_eye_landmarks, right_eye_landmarks = get_eye_landmarks(face_landmarks)

        # Draw left eye landmarks
        for landmark in left_eye_landmarks:
            x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
            cv2.circle(annotated_image, (x, y), 1, (0, 255, 0), -1)

        # Draw right eye landmarks
        for landmark in right_eye_landmarks:
            x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
            cv2.circle(annotated_image, (x, y), 1, (0, 255, 0), -1)

    return annotated_image

font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to read camera feed")
    sys.exit(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    s = time.time()
    ret, img = cap.read()
    
    if not ret:
        print('WebCAM Read Error')
        break

    annotated = get_face_mesh(img)
    e = time.time()
    fps = 1 / (e - s)
    cv2.putText(annotated, 'FPS:%5.2f' % fps, (10, 50), font, fontScale=1, color=(0, 255, 0), thickness=1)
    cv2.imshow('webcam', annotated)
    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
