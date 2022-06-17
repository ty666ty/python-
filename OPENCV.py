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

class PyQtMainEntry(QMainWindow, Ui_MainWindow):


    #使用**cv.imread**()函数读取图像。图像应该在工作目录或图像的完整路径应给出。
    # 第二个参数是一个标志，它指定了读取图像的方式。
    #
    # cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
    # cv.IMREAD_GRAYSCALE：以灰度模式加载图像
    # cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    # 注意 除了这三个标志，你可以分别简单地传递整数1、0或-1。
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.camera = cv2.VideoCapture(0)
        # self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        # self._timer = QtCore.QTimer(self)
        # self._timer.timeout.connect(self._queryFrame)
        # self._timer.setInterval(30)


    def btnReadImage_Clicked(self):
        '''
        从本地读取图片
        '''
        # 打开文件选取对话框
        filename, _ = QFileDialog.getOpenFileName(self, '打开图片')
        if filename:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnGray_Clicked(self):
        '''
        灰度化
        '''
        # 如果没有捕获图片，则不执行操作
        if not hasattr(self, "captured"):
            return

        self.cpatured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnThreshold_Clicked(self):
        '''
        Otsu自动阈值分割
        '''
        if not hasattr(self, "captured"):
            return

        _, self.cpatured = cv2.threshold(
            self.cpatured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()

        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols

        cv.cvtColor(self.frame, cv.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



    def cv_save(name, img):  # 保存图片
        cv2.imwrite(name, img)

    def cv_show(name,img):#显示图片
        cv2.imshow(name,img)
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
    #     cv2.imshow('name',img1)
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

    def cv_byjc1(img):#灰度图图边缘检测

        v1 = cv2.Canny(img, 80, 150, (3, 3))
        v2 = cv2.Canny(img, 50, 100, (5, 5))

        # np.vstack():在竖直方向上堆叠
        # np.hstack():在水平方向上平铺堆叠
        ret = np.hstack((v1, v2))
        cv2.imshow('img', ret)
        cv2.waitKey(0)
        cv2.destroyAllWindows()





# if __name__ == '__main__':
#     img = cv2.imread('img/05505.jpg') # 图片读取
#     img1 = cv2.imread('img/05505.jpg',0)#读取灰度图片
#     cv_show('p1',img)
#     cv_fansecai(img)
#     cv_byjc(img)
#     cv_byjc1(img1)
#     cv_suofang(img,400,300)
#     cv_caijian(img,200,600,0,300)
    # cv2.waitKey()  # 窗口等待任意键盘按键输入,0为一直等待,其他数字为毫秒数

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec())

    # cv2.waitKey(0)  # 显示时长








