import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import cv2

img=np.zeros((512,512),np.uint8)#创建全0数组
img[70:170, 110:210] = 155#设置一块区域为全白
cv2.namedWindow('test3-1', cv2.WINDOW_NORMAL)#创建窗口
cv2.imshow('test3-1',img)

img=np.zeros((280,360,3), np.uint8) 		#创建一幅黑色图像
cv2.line(img,(0,0),(320,130),(255,0,0),5)		#画对角线1，蓝色
cv2.line(img,(320,0),(6,300),(0,255,0),5)		#画对角线2，绿色
cv2.rectangle(img,(20,20),(80,80),(216,234,110),-1)
cv2.imshow('da',img)          			#显示图像

img=np.zeros((200,320,3), np.uint8) 		#创建一幅黑色图像
cv2.circle(img,(160,100),80,(255,0,0),5)		#画圆，蓝色边框
cv2.circle(img,(160,100),40,(0,255,0),-1)		#画圆，绿色填充
cv2.imshow('draw',img)          			#显示图像

img=np.zeros((200,320,3), np.uint8)+255 	    #创建一幅白色图像
pts=np.array([[160,20],[20,100],[160,180],[300,100]], np.int32)	#创建顶点
cv2.polylines(img,[pts],True,(255,0,0),5)	  #画多边形，蓝色边框
pts=np.array([[160,60],[60,100],[160,140],[260,100]], np.int32)	#创建顶点
cv2.polylines(img,[pts],False,(0,255,0),8)     #画曲线，绿色
cv2.imshow('draw1',img)

img=np.zeros((200,320,3), np.uint8)+255 		#创建一幅白色图像
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'Python',(50,160),font,2,(255,0,0),2,cv2.LINE_AA)	#绘制文本

cv2.imshow('draw3',img)




cv2.waitKey(0)



