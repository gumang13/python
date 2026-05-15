
import cv2
import numpy as np

img = cv2.imread("opencv_study/images/fill.png")

img = cv2.resize(img,(640,480))
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red1 = np.array( [ 0,100,100] )
up_red1 = np.array([ 10,255,255 ]) 
lower_red2 = np.array( [150,80,80] )
up_red2 = np.array([179,255,255])
lower_yellow = np.array([20,100,100])
up_yellow = np.array([40,255,255])
lower_green = np.array([100,100,100])
up_green = np.array([130,255,255])

mask1 = cv2.inRange(hsv,lower_red1,up_red1)
mask2 = cv2.inRange(hsv,lower_red2,up_red2)
mask3 = cv2.inRange(hsv,lower_yellow,up_yellow)
mask4 = cv2.inRange(hsv,lower_green,up_green)
mask = mask1 + mask2+ mask3 +mask4

kernel= np.ones((5,5),np.uint8)

mask = cv2.morphologyEx(
    mask , cv2.MORPH_OPEN ,kernel,iterations=1
)
mask = cv2.morphologyEx( mask,cv2.MORPH_CLOSE,kernel,iterations=2)
copy_img=img.copy()
contours,_= cv2.findContours(
    mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE
)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(
        copy_img,(x,y),(x+w,y+h),(0,255,0),2
    )
cv2.imshow("img",img)
cv2.imshow("result",copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
