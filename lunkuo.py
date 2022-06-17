import cv2
import numpy as np
import matplotlib as plt

img=cv2.imread('cat.jpg',0)
cv2.imshow('yuantu',img)

img2=cv2.Canny(img,200,300)
cv2.imshow('Canny',img2)

ret,img3=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
c,h=cv2.findContours(img3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print('轮廓:',c)
print('轮廓类型:',type(c))
print('轮廓数:',len(c))
print('层次',h)
print('层次类型:',type(h))

# img4 = np.zeros_like(img) + 255
# for n in (range(len(c))):
# 	cv2.polylines(img4,[c[n]],True,(255,0,0),2)
# cv2.imshow('%s'%n,img4)


img5=np.zeros(img.shape,np.uint8)+255
img5=cv2.drawContours(img3,c,-1,(0,0,255),2)
cv2.imshow('Contours',img5)

for n in range(len(c)):
	m=cv2.moments(c[n])
	print('轮廓%s的矩：'%n,m)
	print('轮廓%s的面积：' % n, m['m00'])

img=cv2.imread('cat.jpg')#读取图像
cv2.imshow('original',img)#显示原图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将其转化为灰度图像
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)#二值化阈值处理
c,h=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#查找轮廓

img3=np.zeros(img.shape,np.uint8)+255
img3=cv2.drawContours(img3,c,-1,(0,0,255),2)
cv2.imshow('Counters',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()
