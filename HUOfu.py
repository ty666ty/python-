import cv2
import  numpy as np
# img=cv2.imread('05501.jpg')
# o=img.copy()
# o=cv2.medianBlur(o,5)
# gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
# binary=cv2.Canny(o,200,350)
# lines=cv2.HoughLinesP(binary,1,np.pi/180,15,minLineLength=100,maxLineGap=15)
# for line in lines:
#     x1,y1,x2,y2=line[0]
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# cv2.imshow('canny',binary)
# cv2.imshow('img',img)

img=cv2.imread('O.jpg')
o=img.copy()
o=cv2.medianBlur(o,5)
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,60,param1=200,param2=20,minRadius=10,maxRadius=30)
circles=np.uint(np.around(circles))
for c in circles[0]:
    x,y,r=c
    cv2.circle(img,(x,y),r,(0,0,255),3)
    cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

