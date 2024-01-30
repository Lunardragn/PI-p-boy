# Import all important functionality
import cv2
import mediapipe as mp

# Start cv2 video capturing through CSI port
cap = cv2.VideoCapture(0)

# Initialise Media Pipe Pose and Hand features
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
pose = mp_pose.Pose()
hands = mp_hands.Hands()

# Start endless loop to create video frame by frame
while True:
    ret, frame = cap.read()
    flipped = cv2.flip(frame, flipCode=1)
    frame1 = cv2.resize(flipped, (640, 480))
    rgb_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    
    # Process the image to detect pose and hands
    pose_results = pose.process(rgb_img)
    hands_results = hands.process(rgb_img)
    
    # Draw pose landmarks on the frame
    if pose_results.pose_landmarks:
        mpDraw.draw_landmarks(frame1, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Draw hand landmarks on the frame
    if hands_results.multi_hand_landmarks:
        for hand_landmarks in hands_results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame1, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Show the processed frame with pose and hand landmarks
    cv2.imshow("frame", frame1)
    
    # At any point if the 'esc' key is pressed on the keyboard, the system will stop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
