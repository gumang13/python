
import cv2

img = cv2.imread("opencv_study/images/carrr.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bler = cv2.GaussianBlur(gray,(19,19),0)
_,thresh=cv2.threshold(
    bler,130,255,cv2.THRESH_BINARY_INV
)
contours,heir = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
result=img.copy()

cv2.drawContours(
    result,contours,-1,(0,0,255),2
)
print(f"찾은 차량의 수 : {len(contours)}")

cv2.imshow("result",result)
cv2.imshow("contours",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
