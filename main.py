import sys

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):#定义了一个PyQtMainEntry类
    def __init__(self):#初始化
        super().__init__()
        self.setupUi(self)


    # def openimage(self):
    #     imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
    #     jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
    #     self.label.setPixmap(jpg)

    def btnReadImage_Clicked(self):#打开图片槽函数
        filename, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        self.captured = cv.imread(str(filename))
        self.captured1=cv.imread(str(filename),0)

        jpg = QtGui.QPixmap(filename).scaled(self.label_b.width(), self.label_b.height())
        self.label_b.setPixmap(jpg)

    def btnReadImage_Clicked1(self):
        '''
        从本地读取图片
        '''
        # 打开文件选取对话框
        filename, _ = QFileDialog.getOpenFileName(self, '打开图片')
        if filename:
            self.captured = cv.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv.cvtColor(self.captured, cv.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.label_b.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_b.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



    def btnGray_Clicked(self):
        '''
        灰度化
        '''
        if not hasattr(self, "captured"):
            return
        # self.gray=self.captured1
        cv.imshow('dst',self.captured1)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def btnSave1_Clicked(self):
        if not hasattr(self, "captured"):
            return
        lj = self.lineEdit_2.text()
        print('保存路径为', lj)
        cv.imwrite(lj,self.captured1)
        print('保存成功')

    def btnFanse(self):#反色图片   速度快
        src = self.captured
        if src is None:
            return
        dst = cv.bitwise_not(src)  # 按位取反
        self.fanse = dst
        cv.imshow('dst', dst)
        cv.waitKey()

    def btnFanse1(self):#反色图片  速度慢
        if not hasattr(self, "captured"):
            return
        cha = self.captured.shape
        height, width, deep = cha
        dst = np.zeros((height, width, 3), np.uint8)
        for i in range(height):  # 色彩反转  FOR循环
            for j in range(width):
                b, g, r = self.captured[i, j]
                dst[i, j] = (255 - b, 255 - g, 255 - r)

        self.fanse=dst
        cv.imshow('dst', dst)
        cv.waitKey()


    def btnSave2_Clicked(self):
        if not hasattr(self, "captured"):
            return
        lj = self.lineEdit_3.text()
        print('保存路径为', lj)
        cv.imwrite(lj,self.fanse)
        print('保存成功')

    def btnByjc(self):

            # Canny边缘检测
            byjc=self.captured1

            v1 = cv.Canny(byjc, 80, 150, (3, 3))#输入的图片应该为单通道灰度图
            v2 = cv.Canny(byjc, 50, 100, (5, 5))

            # np.vstack():在竖直方向上堆叠
            # np.hstack():在水平方向上平铺堆叠
            self.ret = np.hstack((v1,v2))
            # self.ret = cv.Canny(byjc, 599, 600)
            cv.imshow('img',self.ret)
            cv.waitKey(0)
            cv.destroyAllWindows()

    # Canny边缘检测
    def btnByjc1(self):
        src = self.captured1
        # if src is None:
        #     return

        blurred = cv.GaussianBlur(src, (3, 3), 0)
        gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

        grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
        grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

        dst = cv.Canny(grad_x, grad_y, 50, 150)
        self.ret=dst
        # dst = cv.Canny(gray, 50, 150)

    def btnSave3_Clicked(self):
        if not hasattr(self, "captured"):
            return
        lj = self.lineEdit_4.text()
        print('保存路径为', lj)
        cv.imwrite(lj,self.ret)
        print('保存成功')

    def btnSuofang(self):#缩放图片
        x,y=int(self.lineEdit.text()), int(self.lineEdit_5.text())
        img=self.captured
        dst = cv.resize(img, (x, y))
        self.suofang=dst
        cv.imshow("dst: %d x %d" % (dst.shape[0], dst.shape[1]), dst)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def btnSave4_Clicked(self):
        if not hasattr(self, "captured"):
            return
        lj=self.lineEdit_6.text()
        print('保存路径为',lj)
        cv.imwrite(lj,self.suofang)
        print('保存成功')

    def btnCut(self):
        if not hasattr(self, "captured"):
            return
        img=self.captured
        y0, y1 = int(self.lineEdit_y0.text()), int(self.lineEdit_y1.text())
        x0, x1 =  int(self.lineEdit_x0.text()), int(self.lineEdit_x1.text())

        dst = img[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
        self.cut=dst
        cv.imshow('image', dst)
        cv.waitKey(0)


    def btnSave5_Clicked(self):
        if not hasattr(self, "captured"):
            return
        pathway = self.lineEdit_12.text()
        print('保存路径为', pathway)
        cv.imwrite(pathway,self.cut)
        print('保存成功')



    def btnThreshold_Clicked(self):
        '''
        Otsu自动阈值分割
        '''
        if not hasattr(self, "captured"):
            return
        img=self.captured1
        #th1 = cv.threshold(img, int(self.lineEdit_7.text()), 255, cv.THRESH_BINARY)
        #th2 = cv.adaptiveThreshold(
            #img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 4)
        #self.yz=th2
        #th3 = cv.adaptiveThreshold(
            #img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 6)
        #yuz,max=int(self.lineEdit_7.text()), int(self.lineEdit_8.text())
        dst,self.yuzhi=cv.threshold(img, int(self.lineEdit_7.text()), 255, cv.THRESH_BINARY)
        print(int(self.lineEdit_7.text()))
        # self.yuzhi = cv.adaptiveThreshold(#自适应阈值
        #     img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 6)
                        #参数说明如下。
                            #dst为阈值处理的结果图像。/src为原图像。/maxValue为最大值。
                            #adaptiveMethod为自适应方法，其值为cv2.ADAPTIVE_THRESH_MEAN_C（邻域中所有像素点的权重值相同）或者cv2.ADAPTIVE_THRESH_GAUSSIAN_C（邻域中像素点的权重值与其到中心点的距离有关，通过高斯方程可计算各个点的权重值）。
                            #thresholdType为阈值处理方式，其值为cv2.THRESH_BINARY（二值化阈值处理）或者cv2.THRESH_BINARY_INV（反二值化阈值处理）。
                            #blockSize为计算局部阈值的邻域的大小。
                            #C为常量，自适应阈值为blockSize指定邻域的加权平均值减去C。


        # self.cpatured = cv.threshold(
        #     self.cpatured, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        #
        # rows, columns = self.cpatured.shape
        # bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8

        cv.imshow('dst', self.yuzhi)
        # cv.imshow('dst',th2)
        # cv.imshow('dst', th3)
        cv.waitKey(0)
        # self.label_b.setPixmap(QPixmap.fromImage(QImg).scaled(
        #     self.label_b.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnSave6_Clicked(self):
        if not hasattr(self, "captured"):
            return
        pathway = self.lineEdit_11.text()
        print('保存路径为', pathway)
        cv.imwrite(pathway,self.yuzhi)
        print('保存成功')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()#显示主窗口
    sys.exit(app.exec())
