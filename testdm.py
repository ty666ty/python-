import sys
import cv2
import PyQt6
import numpy as np
import matplotlib.pyplot as plt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow

def cv_save(name, img):  # 保存图片
        cv2.imwrite(name, img)

def cv_show(name,img):#显示图片
        cv2.imshow(name,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def cv_gray(name,filename):
    img=cv2.imread(filename,0)
    cv2.imshow(1,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cv_suofang(img,x,y):

        # 缩放图像，后面的其他程序都是在这一行上改动
        dst = cv2.resize(img, (x, y))
        # 显示图像
        cv2.imshow("dst: %d x %d" % (dst.shape[0], dst.shape[1]), dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def cv_caijian(img,y0,y1,x0,x1):
        dst = img[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imshow('image', dst)
        cv2.waitKey(0)


    # def cv_show(name,img,x):#显示图片
    #     if (x==1):#显示彩图
    #         cv2.imshow(name,img)
    #         cv2.waitKey(0)

    #         cv2.destroyAllWindows()
    #     elif(x==0):#显示灰度图
    #         img=cv2.imread(img,0)
    #         cv2.imshow(name, img)
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()
    #     else:
    #         print("参数有误，请重试")


    # def cv_hshow(name,img):#显示灰色图片
    #     img1 = cv2.imread(img, 0)
    #     cv2.imshow('name',img1,)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()


def cv_fansecai(img):#反色图片

        cha = img.shape
        height, width, deep = cha
        dst = np.zeros((height, width, 3), np.uint8)
        for i in range(height):  # 色彩反转
            for j in range(width):
                b, g, r = img[i, j]
                dst[i, j] = (255 - b, 255 - g, 255 - r)

        cv2.imshow('dst', dst)
        cv2.waitKey()

def cv_byjc(img):#彩图边缘检测
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 1, 2), plt.imshow(sobelx, cmap='gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 1, 3), plt.imshow(sobely, cmap='gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        plt.show()

def cv_byjc1(img):#边缘检测

        v1 = cv2.Canny(img, 80, 150, (3, 3))
        v2 = cv2.Canny(img, 50, 100, (5, 5))

        # np.vstack():在竖直方向上堆叠
        # np.hstack():在水平方向上平铺堆叠
        ret = np.hstack((v1, v2))
        cv2.imshow('img', ret)
        cv2.waitKey(0)
        cv2.destroyAllWindows()





if __name__ == '__main__':
    img = cv2.imread('img/05505.jpg') # 图片读取
    img1 = cv2.imread('img/05505.jpg',0)#读取灰度图片
    cv_show('p1',img)

    # cv_fansecai(img)
    # cv_byjc(img)
    cv_byjc1(img1)
    cv_suofang(img,400,300)
    cv_caijian(img,200,600,0,300)
    # cv2.waitKey()  # 窗口等待任意键盘按键输入,0为一直等待,其他数字为毫秒数