import cv2
import numpy as np
import matplotlib as plt
img=cv2.imread('chuyinx.jpg',0)
cv2.imshow('1',img)

lpls=np.array([[0,1,0],[1,-4,1],[0,1,0]])
img2=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('Laplacian',img2)
img5=cv2.filter2D(img,-1,lpls)
cv2.imshow('lplsjjh',img5)

# for i in range(img.shape[0]):
# 	for j in range(img.shape[1]):
# 		for k in range(img.shape[2]):
# 			img[i,j,k]=
img3=cv2.Sobel(img,cv2.CV_8U,0,1)
cv2.imshow('Sobel',img3)
Sobx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Soby=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
img6=cv2.filter2D(img,-1,Sobx)
img7=cv2.filter2D(img,-1,Soby)
cv2.imshow('sobjj',img7)

img4=cv2.Canny(img,150,200)
cv2.imshow('Canny',img4)

# img_g=cv2.GaussianBlur(img,(5,5),0,0)
# img7=cv2.filter2D(img_g,-1,Sob)
# cv2.imshow('Cannyjjh',img7)

cv2.waitKey(0)