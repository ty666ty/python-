import cv2
import numpy as np

img=cv2.imread('chuyinx.jpg')
img3=img
img4=img3

cv2.imshow('yt',img)#显示原图像
img1 = cv2.flip(img, 0)#用opcv方法翻转图片上下
cv2.imshow('cv',img1)

img2=img[::-1,::,::]#用切片翻转上下
cv2.imshow('qp',img2)

ret = np.zeros_like(img) #创建一个空图
for i in range(0,img.shape[0]):
        ret[img.shape[0]-i-1,:] = img[i,:]  #翻转
cv2.imshow('for',ret)


cv2.waitKey(0)
#
# while True:
#     key=cv2.waitKey()
#     if key==48: 			#按【0】键时显示原图
#         img2=img
#     elif key==49: 			#按【1】键时垂直翻转
#         img2=cv2.flip(img,0)
#     elif key==50: 			#按【2】键时水平翻转
#         img2=cv2.flip(img,1)
#     elif key==51: 			#按【3】键时水平、垂直翻转
#         img2=cv2.flip(img,-1)
#     elif key==52:
#         img2=img[::-1,::,::]
#     cv2.imshow('showimg',img2)

# while True:
# 		key = cv2.waitKey()
# 		if 48 <= key <= 53:  # 按键【0】【1】【2】【3】或【4】
# 			x = y = sc[key - 48]  # 获得缩放比例
# 			img2 = cv2.resize(img, None, fx=x, fy=y)  # 缩放图像
# 			cv2.imshow('showimg', img2)  # 显示图像
# 		#
		# elif 54<=key<=56:
		# 		x = y = sc[key - 48]  # 获得缩放比例
		# 		img2 = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_CUBIC)  # 缩放图像
		# 		cv2.imshow('showimg',img2)

