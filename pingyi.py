import cv2
import numpy as np
img=cv2.imread('chuyinx.jpg')

cv2.imshow('img',img)#显示原图像

height=img.shape[0]
width=img.shape[1]

dsize = (width,height)
m=np.float32([[1,0,100],
			  [0,1,100]])
img_cv2 = cv2.warpAffine(img,m,dsize)
cv2.imshow('cv',img_cv2)

img1 = np.zeros(img.shape, np.uint8)
img1[100:428,100:330] = img[0:328,0:230]
cv2.imshow('qp',img1)

img_for = img
img3 = np.zeros(img.shape, np.uint8)
for i in range(img_for.shape[0]-100):
    for j in range(img_for.shape[1]-100):
        img3[i+100,j+100] = img_for[i, j]
cv2.imshow('for',img3)

cv2.waitKey(0)


