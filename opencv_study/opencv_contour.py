
# contour 는 연결된 외곽선 이다 . 
# edge 가 경계선 이라면 contour는 연결된 객체의 외곽선 묶음 이다.
# contour 를 사용하면 이미지 안에서 객체의 영역을 찾을 수 있다.
# treshold 나 edge 로 동전과 배경을 분리하고 contour로 찾는다.

import cv2

img = cv2.imread("opencv_study/images/coin.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
_,thresh = cv2.threshold(
    blur,131,255, cv2.THRESH_BINARY_INV
) 
#contour 를 하기 전에 Canny 나 threshold로 경계 영역을 만들어야 한다.

# cv2.findContours - 발견된 영역에서 가장 바깥쪽 외곽선만 찾는다.
# cv2.RETR_EXTERNAL - 동전의 가운데가 검은색으로 표시되도 바깥쪽 외곽만 사용한다.
# cv2.CHAIN_APPROX_SIMPLE - 외곽선을 저장 할 때 필요한 부분만 저장하기
#    findContour( 이미지값 , mode , method )
#    mode매개변수에 들어갈 값
#       cv2.RETR_LIST : 모든 contour 를 찾기 
#       cv2.RETR_TREE : 모든 contour를 찾고 계층관계까지 저장
#       cv2.RETR_CCOMP : 2계층으로 저장 ( 예 - 도넛을 인식하는 경우 도넛 외곽과 가운데 구멍까지 만 저장 ) 
#       findContours함수의 두번째 반환값은 계층 정보가 반환된다.
#       두번째 반환값으로 [next(같은계층 contour), pre(같은계층의 이전 contour),
#                          first_child(안쪽계층의 첫번재 자식 contour),
#                          parent(현재 contour의 부모 contour)]

# findContours 함수 3번째 인자 method
#   cv2.CHAIN_APPROX_NONE : 외곽선의 모든 픽셀 좌표저장(정밀분석)
#   cv2.CHAIN_APPROX_TC89_L1 : teh-chain 알고리즘 기반- 더 부드럽게 표시하기 위한 
contours,hier = cv2.findContours(
    thresh , 
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result=img.copy()

# drawContours( 이미지 , contours , 어떤contour에 그리는가? , 색상 , 선두께)

cv2.drawContours( result,contours,-1,(0,0,255),2)

print(f"찾은 동전의 수 : {len(contours)}")

cv2.imshow("thr",thresh)
cv2.imshow("contours",result)
cv2.waitKey(0)
cv2.destroyAllWindows()