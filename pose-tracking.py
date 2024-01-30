#Import all important functionality
import cv2
import mediapipe as mp

#Start cv2 video capturing through CSI port
cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose()

#Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
while True:
    ret,frame=cap.read()
    flipped=cv2.flip(frame,flipCode=1)
    frame1 = cv2.resize(flipped,(640,480))
    rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    result=pose.process(rgb_img)
    #Print general details about observed body
    print (result.pose_landmarks)
    
    #Uncomment below to see X,Y coordinate Details on single location in this case the Nose Location.
    
    #try:
    #    print('X Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640)
    #    print('Y Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480)
    #except:
    #    pass
    
    #Draw the framework of body onto the processed image and then show it in the preview window
    mpDraw.draw_landmarks(frame1,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("frame",frame1)
    
    #At any point if the | q | is pressed on the keyboard then the system will stop
    key = cv2.waitKey(1) & 0xFF
    if key ==ord("q"):
        break
        
