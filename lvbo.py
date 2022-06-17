import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,2,1)
img=cv2.imread('chuyinx.jpg',0)
plt.imshow(img,cmap='gray')


plt.subplot(2,2,2)
img2=cv2.blur(img,(5,5))		#可调整卷积核大小以查看不同效果
plt.imshow(img2,cmap='gray')


plt.subplot(2,2,3)
x=img.shape[0]
y=img.shape[1]
img_h=np.zeros_like(img)           #for循环实现
img_g=np.zeros_like(img)
for i in range(x-2):
	for j in range(y-2):

		img_h[i+1,j+1]=np.sum(img[i:i+5,j:j+5])/25

plt.imshow(img_h,cmap='gray')

plt.subplot(2,2,4)
kernal = np.ones((5, 5), np.float32) / 25#自定义卷积核
dst = cv2.filter2D(img, None, kernal)
plt.imshow(img_h,cmap='gray')
plt.show()






	#可调整卷积核大小以查看不同效果,均值滤波




#
# img3=cv2.GaussianBlur(img,(5,5),0,0)			#可调整卷积核大小以查看不同效果  高斯
# cv2.imshow('imgBlur1',img3)
#
#
# img4=cv2.boxFilter(img,-1,(2,2),normalize=False) 	  #可调整卷积核大小以查看不同效果  方框
# cv2.imshow('imgBlur4',img4)
#
# img5=cv2.medianBlur(img,23)		#可调整卷积核大小以查看不同效果  中值
# cv2.imshow('imgBlur5',img5)
#
#
# img6=cv2.bilateralFilter(img,20,100,100)		#可调整参数以查看不同效果
# cv2.imshow('6',img6)



