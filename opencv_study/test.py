
import cv2

cap = cv2.VideoCapture("opencv_study/videos/motion_car.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps) 
pre_frame = None

while True:
    ret , frame = cap.read()
    if not ret :
        continue
    frame = cv2.resize(frame,(480,640))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if pre_frame is None:
        pre_frame=gray
        continue

    diff = cv2.absdiff(pre_frame,gray)

    _,thresh = cv2.threshold(
        diff,80,255,cv2.THRESH_BINARY
    )

    thresh = cv2.dilate( thresh , None , iterations=2)

    contours,_ = cv2.findContours(
        thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE
    )

    result=frame.copy()
    for con in contours:
        x,y,w,h=cv2.boundingRect(con)
        cv2.rectangle(
            result,
            (x,y),
            (x+w,y+h),
            (0,0,255),
            2
        )
    cv2.imshow("result",result)
    cv2.imshow("diff",diff)
    cv2.imshow("frame",frame)
    if cv2.waitKey(33)==27:
        break
    pre_frame=gray
cap.releas()
cv2.destroyAllWindows()



    
