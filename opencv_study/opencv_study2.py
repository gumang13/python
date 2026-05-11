

# AI가 영상 분석을 하는데 먼저 전처리 과정을 거친다.
# 전처리는 크기변경 , 흑백변환, 노이즈 제거, 강조 처리 등 
 
import cv2

# img = cv2.imread("opencv_study/images/surfer.png")

# 변경 이후에 show
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("surfer",gray)
# print(gray.shape)
# print( gray[100][100] )
# cv2.waitKey(0)

# 크기 변경 하기 

# small = cv2.resize(img, (500,100) )
# cv2.imshow("size",small)
# cv2.waitKey(0)


# 이미지 뒤집기 (반전) 
# flip = cv2.flip(img, 1)
# # 1 - 좌우 반전 , 0 - 상하 반전 , -1 - 상하좌우 반전 
# cv2.imshow("flip",flip)
# cv2.waitKey(0)

# 블러 처리 - 이미지를 흐리게 만드는것
# 노이즈 감소의 목적
# 

# blur = cv2.GaussianBlur( img, (5,5) , 0)
# # (5,5) 의 값을 크게 주면 더더 흐려진다.

# cv2.imshow("blur",blur)
# cv2.waitKey(0)

# # 경계 - threshold 
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# _r, thresh = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY
# )
# _r, thresh_rev = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY_INV
# )
# print(_r)
# cv2.imshow("gray",gray)
# cv2.imshow("bin",thresh)
# cv2.imshow("inv",thresh_rev)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 사진의 크기는 가로길이 320으로 비율 유지해서 변경하고
# 흑백 변환하고 , 멍멍이가 잘 보일 수 있도록 경계설정 하여
# dog_result.png로 저장 
#  1512:2016 = x : 320   >  x= 1512*320/2016
# img_ = cv2.imread("opencv_study/images/dog.png")
# print(img_.shape)
# img = cv2.resize(img_,(320,1512*320//2016))
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# _r, thresh = cv2.threshold(
#     gray, 130, 255, cv2.THRESH_BINARY
# )
# cv2.imshow("result",thresh)
# cv2.waitKey(0)
# cv2.imwrite("opencv_study/images/dog_result.png",thresh)

img = cv2.imread("opencv_study/images/dog.png")
y,x = img.shape[:2]
re_img=cv2.resize(img,(400,400*x//y))
blr= cv2.GaussianBlur(re_img,(7,7),0)
gray = cv2.cvtColor(blr,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(
    gray , 100 , 255 , cv2.THRESH_BINARY
)
cv2.imshow("result",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
