

import cv2
cap = cv2.VideoCapture("opencv_study/videos/bird.mp4")

# 영상 정보
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_cnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# 특정 시간의 영상 캡처하기 ( 프레임 저장 )
target_sec = 5

target_frame_num = int(fps*target_sec)

cap.set(
    cv2.CAP_PROP_POS_FRAMES,target_frame_num
)
ret , frame = cap.read()
cv2.imwrite("저장경로와 파일명",frame)
print(f"w : {width} , h : {height}, fps : {fps}, 총 프레임 수 : {frame_cnt}")
frame_idx=0
while True:
    ret , frame = cap.read() # 프레임 잙 읽었나 ? , 이미지 한장
    if not ret:
        break
    
    small = cv2.resize(frame,(540,960))
    # cv2.rectangle(
    #     small,(50,50),(250,250),(0,0,255),-1
    # )
    # small[50:250,50:250]=(0,0,255)
    gray = cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)
    if frame_idx == target_frame_num: 
        cv2.imwrite("opencv_study/images/bird.png",frame)
    
    
    cv2.imshow("bird",gray)

    if cv2.waitKey(30) == 27:  # esc키 코드는 27이다.  ( 종료를 함 )
        break
    frame_idx +=1  # 프레임 번호 
cap.release()  # 영상 파일이나 카메라의( 메모리 닫기 )
cv2.destroyAllWindows()
