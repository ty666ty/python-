import cv2
import numpy as np


def ImageHist(image, type):
	color = (255, 255, 255)
	windowName = 'Gray'
	if type == 31:
		color = (255, 0, 0)
		windowName = 'B Hist'
	elif type == 32:
		color = (0, 255, 0)
		windowName = 'G Hist'
	elif type == 33:
		color = (0, 0, 255)
		windowName = 'R Hist'
	# 这个方法是用来计算图片的直方图 1 image 图片的数据 2 [0] 用于计算直方图的通道 灰度直方图 所以就用第一个通道
	# 3 mask 模板 4 直方图的size 表明直方图分成多少份或者是有多少个柱状 总共256种灰度值 5 表明直方图中各个像素的值 0-255 所有的像素都遍历一次
	# 灰度值只能是0-255这个范围内

	hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
	minV, maxV, minL, maxL = cv2.minMaxLoc(hist)  # 最小值,最大值,最小值的下标,最大值的下标
	# 创建一个画布 三维画布
	histImg = np.zeros([256, 256, 3], np.uint8)  # (r,g,b) 3 rgb三个颜色 矩阵数据
	# for循环 依次把这个画布给它画一下
	for h in range(256):  # 表明总共有0-255这么多点
		intenNormal = int(hist[h] * 256 / maxV)  # 规划数据,因为我们的值很大,所以我们要把它规划一下 hist[h]获取每一个直方图的数据
		# hist[h]*256/maxV,这样经过计算完之后它的值就会归一到0-256之间
		cv2.line(histImg, (h, 256), (h, 256 - intenNormal), color)  # histImg矩阵数据 整个循环的下标 整个图片的范围是0-256之间 256减去当前的规划之后的值
	cv2.imshow(windowName, histImg)
	return histImg


img = cv2.imread('image0.jpg', 1)  # 读取的是彩色图片
channels = cv2.split(img)  # 获取每一个通道 channels 获取当前的通道 通过split的方法完成图像的分解 RGB - R G B 三个颜色通道
for i in range(0, 3):  # for循环遍历每个颜色通道
	ImageHist(channels[i], 31 + i)
cv2.waitKey(0)