import cv2
import sys
import time
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

def eye_aspect_ratio(eye_landmarks):
    # Compute the Euclidean distances between the two sets of vertical eye landmarks
    A = np.linalg.norm(np.array([eye_landmarks[1].x, eye_landmarks[1].y]) - np.array([eye_landmarks[5].x, eye_landmarks[5].y]))
    B = np.linalg.norm(np.array([eye_landmarks[2].x, eye_landmarks[2].y]) - np.array([eye_landmarks[4].x, eye_landmarks[4].y]))
    # Compute the Euclidean distance between the horizontal eye landmarks
    C = np.linalg.norm(np.array([eye_landmarks[0].x, eye_landmarks[0].y]) - np.array([eye_landmarks[3].x, eye_landmarks[3].y]))
    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

def get_eye_region(image, eye_landmarks):
    # Convert the eye landmarks to numpy array
    eye_landmarks = np.array([(landmark.x * image.shape[1], landmark.y * image.shape[0]) for landmark in eye_landmarks], dtype=np.int32)
    # Create a mask to extract the region of interest (ROI) around the eye
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [eye_landmarks], (255, 255, 255))
    # Bitwise AND operation to extract the ROI
    eye = cv2.bitwise_and(image, mask)
    return eye

def get_pupil_position(eye):
    # Convert to grayscale
    gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blurred_eye = cv2.GaussianBlur(gray_eye, (7, 7), 0)
    # Thresholding to binarize the image
    _, threshold = cv2.threshold(blurred_eye, 50, 255, cv2.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Find the contour with maximum area (the pupil)
    if contours:
        pupil_contour = max(contours, key=cv2.contourArea)
        # Compute the moments of the contour to find the centroid (pupil position)
        moments = cv2.moments(pupil_contour)
        pupil_position = (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))
        return pupil_position
    else:
        return None

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

        left_eye_landmarks = face_landmarks.landmark[133:143]
        right_eye_landmarks = face_landmarks.landmark[362:374]

        left_eye_ear = eye_aspect_ratio(left_eye_landmarks)
        right_eye_ear = eye_aspect_ratio(right_eye_landmarks)

        # Check if eyes are closed (EAR below threshold)
        if left_eye_ear < 0.2 and right_eye_ear < 0.2:
            continue  # Skip pupil detection if eyes are closed

        left_eye = get_eye_region(annotated_image, left_eye_landmarks)
        right_eye = get_eye_region(annotated_image, right_eye_landmarks)

        # Get pupil positions
        left_pupil = get_pupil_position(left_eye)
        right_pupil = get_pupil_position(right_eye)

        # Draw pupil positions if detected
        if left_pupil:
            cv2.circle(annotated_image, left_pupil, 3, (0, 0, 255), -1)
        if right_pupil:
            cv2.circle(annotated_image, right_pupil, 3, (0, 0, 255), -1)

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
