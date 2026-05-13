
import cv2
import numpy as np
cap = cv2.VideoCapture("opencv_study/videos/walk.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps) 
pre_frame = None

while True:
    ret , frame = cap.read()
    if not ret:
        continue

    frame = cv2.resize(frame,(640,480))
    blur = cv2.GaussianBlur(frame,(5,5),0)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    if pre_frame is None:
        pre_frame = gray
        continue
    diff = cv2.absdiff(pre_frame,gray)

    _ , thresh = cv2.threshold(
        diff , 20,255,cv2.THRESH_BINARY
    )

    # morphology 작업 하기 - 끊어진 부분들을 연결 시키기 
    kernel = np.ones((5,5),np.uint8)

    # 노이즈 제거
    opened = cv2.morphologyEx(
        thresh,cv2.MORPH_OPEN,           # 제거
        kernel,iterations=2
    )

    # 끊어 진 영역 연결
    linked = cv2.morphologyEx(
        opened , cv2.MORPH_CLOSE ,       # 끊어진부분 연결  위해서 채움 작업 
        kernel,iterations=2
    )

    thresh = cv2.dilate(linked ,kernel , iterations=5)
    
    contours , _ = cv2.findContours(
        thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE
    )
    result = frame.copy()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # if area <1000:
        #     continue
        x,y,w,h = cv2.boundingRect(cnt)
        if w*2>h:
            continue
        cv2.rectangle(
            result,
            (x,y),(x+w,y+h),
            (0,0,255),2)
        break
cap.release()
cv2.destroyAllWindows()

    