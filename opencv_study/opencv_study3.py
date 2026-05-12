

# 엣지 디텍션, 콘투어 , 바운딩박스
# 엣지 - 이미지에서 색이나 밝기가 갑자기 변경되는 경계선 

# edge detection 사용되는곳 - 차선 인식, 문서 스캔, 얼굴 인식
#                            로봇의 눈역할, 공장스캔 ( 부품균열, 흠집)

import cv2
# 차선 찾기
img = cv2.imread("opencv_study/images/lane.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

# Canny(이미지값 , 낮은기준값 , 높은기준값)

edge = cv2.Canny(blur , 100 , 200)

cv2.imshow("lane",gray)
cv2.imshow("edge",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()