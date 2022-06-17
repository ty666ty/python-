import cv2
import numpy as np

img=cv2.imread('chuyin1 .jpg',0)
# img = cv2.bitwise_not(img)
cv2.imshow('img',img)

k=np.ones((5,5),np.uint8)
s=np.array([[0,0,1,0,0], [0,0,1,0,0],[1,1,1,1,1],
[0,0,1,0,0],[0,0,1,0,0]],dtype=np.uint8)

fus=cv2.erode(img,k,iterations=2)
cv2.imshow('fus',fus)

pengz=cv2.dilate(img,k,iterations=2)
cv2.imshow('pengz',pengz)
# #开运算
# kai=cv2.dilate(fus,k,iterations=2)
# cv2.imshow('kai',kai)
# #闭运算
# bi=cv2.erode(pengz,k,iterations=2)
# cv2.imshow('bi',bi)
#梯度
tidu=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
cv2.imshow('tidu',tidu)
#顶帽
din=





cv2.waitKey(0)