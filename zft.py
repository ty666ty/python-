import cv2
import matplotlib.pyplot as plt
import numpy as np
plt.subplot(2,2,1)
img=cv2.imread("chuyinx.jpg")#读取图片
img_h=cv2.imread("chuyinx.jpg",0)
# #将bgr转rgb
# b,g,r = cv2.split(img)
# img = cv2.merge([r,g,b])
# # print(img)
plt.imshow(img_h,cmap='gray')#显示原图

plt.subplot(2,2,2)
plt.hist(img_h.ravel(),256)      #绘制直方图

plt.subplot(2,2,3)
img2=cv2.equalizeHist(img_h)#限制对比度自适应直方图均衡化
# clahe=cv2.createCLAHE(clipLimit=5)          		#创建CLAHE对象
# img3 = clahe.apply(img_h)
plt.imshow(img2,cmap='gray')

#直方图统计像素点
def hist_img(img):
	hist=[]
	for i in range(256):
		hist.append(0)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			hist[img[i,j]]+=1
	return hist

#bgr转rbg
def bgr2rgb(img):
	b,g,r = cv2.split(img)
	img = cv2.merge([r,g,b])
	return img

plt.subplot(2,2,4)
plt.hist(img2.ravel(),256) 	#绘制直方图
plt.show()
#
#
# plt.subplot(2,2,2)
# histb=cv2.calcHist([img],[0],None,[256],[0,255])		#计算B通道直方图
# histg=cv2.calcHist([img],[1],None,[256],[0,255])		#计算G通道直方图
# histr=cv2.calcHist([img],[2],None,[256],[0,255])		#计算R通道直方图
# plt.plot(histb,color='b')               			#绘制B通道直方图，蓝色
# plt.plot(histg,color='g')               			#绘制G通道直方图，绿色
# plt.plot(histr,color='r')               			#绘制R通道直方图，红色
#
# mask=np.zeros((w,h), np.uint8)				#按原图大小创建一幅黑色图像
# w1=np.int0(w/6)
# w2=np.int0(w*0.75)
# h1=np.int0(h/4)
# h2=np.int0(h*0.75)
# mask[w1:w2,h1:h2]=255               				#设置掩模白色区域
# cv2.imshow('mask',mask)
# plt.subplot(2,2,3)
# histb=cv2.calcHist([img],[0],mask,[256],[0,255])		#计算B通道直方图
# histg=cv2.calcHist([img],[1],mask,[256],[0,255])		#计算G通道直方图
# histr=cv2.calcHist([img],[2],mask,[256],[0,255])		#计算R通道直方图
# plt.plot(histb,color='b')               		#绘制B通道直方图，蓝色
# plt.plot(histg,color='g')               	    #绘制G通道直方图，绿色
# plt.plot(histr,color='r')               		#绘制R通道直方图，红色
#



