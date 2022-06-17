import numpy as np
import cv2
# img=np.zeros((200,700,3), np.uint8) 			#创建一幅黑色图像
# def doChange(x):
#     b=cv2.getTrackbarPos('B','img')
#     g=cv2.getTrackbarPos('G','img')
#     r=cv2.getTrackbarPos('R','img')
#     img[:]=[b,g,r]
# cv2.namedWindow('img')
# cv2.createTrackbar('B', 'img', 0, 255, doChange)  # 创建跟踪栏
# cv2.createTrackbar('G', 'img', 0, 255, doChange)
# cv2.createTrackbar('R', 'img', 0, 255, doChange)
# while (True):
#     cv2.imshow('img', img)  # 显示图像
#     k = cv2.waitKey(1)
#     if k == 27:  # 按【Esc】键时结束循环
#         break
# cv2.destroyAllWindows()
img=cv2.imread('huamo.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
