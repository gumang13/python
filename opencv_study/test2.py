
import cv2
import numpy as np
cap = cv2.VideoCapture("opencv_study/videos/runrun.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps) 
pre_frame = None

while True:
    ret , frame = cap.read()
    if not ret:
        continue

    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_black = np.array([65,35,130])
    up_black = np.array([95,180,255])

    mask = cv2.inRange(hsv,lower_black,up_black)

    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(
        mask , cv2.MORPH_OPEN , kernel,1
    )
    mask = cv2.morphologyEx(
        mask , cv2.MORPH_CLOSE,kernel,2
    )
    contours,_ = cv2.findContours(
        mask , cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE
    )
    box = frame.copy()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # if area>500: continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(
            box,(x,y),(x+w,y+h),(0,255,0),2
        )
    cv2.imshow("original",frame)
    cv2.imshow("result",box)
    if cv2.waitKey(33)==27:
        break
cap.release()
cv2.destroyAllWindows()   
   

    

   
cap.release()
cv2.destroyAllWindows()

    