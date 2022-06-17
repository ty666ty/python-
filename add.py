import cv2
import numpy as np

# img=cv2.imread('cat.jpg')
# img2=cv2.imread('05501.jpg')
# mask=np.zeros((150,150,3),np.uint8)
#
# img_jia=img+img2
# img_add=cv2.add(img,img2)
# img_addw=cv2.addWeighted(img,0.4,img2,0.6,0)
#
#
# cv2.imshow('1',img)
# cv2.imshow('2',img2)
# cv2.imshow('jia',img_jia)
# cv2.imshow('add',img_add)
# cv2.imshow('addw',img_addw)


r=np.zeros((300,300,3),np.uint8)
g=np.zeros((300,300,3),np.uint8)
b=np.zeros((300,300,3),np.uint8)
b[:,:,0]=255
g[:,:,1]=255
r[:,:,2]=255

w1=r+g+b
cv2.imshow('w1',w1)
# x=r[100,100,0] b
# x1=r[100,100,1] g
# x2=r[100,100,2] r
#
# print(x,x1,x2)
# m1=np.ones((3,3))


cv2.imshow('r',r)
cv2.imshow('g',g)
cv2.imshow('b',b)

a=cv2.add(r,g)
w=cv2.add(a,b)
cv2.imshow('a',a)
cv2.imshow('w',w)
cv2.waitKey(0)
