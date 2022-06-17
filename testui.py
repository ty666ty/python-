import sys
import cv2 as cv
import matplotlib.pyplot as plt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFileDialog, QMainWindow
import numpy as np


from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
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
        self.gray=self.captured1
        cv.imshow('dst',self.gray)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def btnSave1_Clicked(self):
        if not hasattr(self, "captured"):
            return
        cv.imwrite('gray.jpg',self.gray)
        print('保存成功')

    def btnFanse(self):#反色图片   速度快
        src = self.captured
        if src is None:
            return
        dst = cv.bitwise_not(src)  # 按位取反，白变黑，黑变白
        self.fanse = dst
        cv.imshow('dst', dst)
        cv.waitKey()

    def btnFanse1(self):#反色图片  速度慢
        if not hasattr(self, "captured"):
            return
        cha = self.captured.shape
        height, width, deep = cha
        dst = np.zeros((height, width, 3), np.uint8)
        for i in range(height):  # 色彩反转
            for j in range(width):
                b, g, r = self.captured[i, j]
                dst[i, j] = (255 - b, 255 - g, 255 - r)

        self.fanse=dst
        cv.imshow('dst', dst)
        cv.waitKey()


    def btnSave2_Clicked(self):
        if not hasattr(self, "captured"):
            return

        cv.imwrite('fanse.jpg',self.fanse)
        print('保存成功')

    def btnByjc(self):

            # Canny边缘检测
            byjc=self.captured

            v1 = cv.Canny(byjc, 80, 150, (3, 3))
            v2 = cv.Canny(byjc, 50, 100, (5, 5))

            # np.vstack():在竖直方向上堆叠
            # np.hstack():在水平方向上平铺堆叠
            self.ret = np.hstack((v1,v2))
            cv.imshow('img',self.ret)
            cv.waitKey(0)
            cv.destroyAllWindows()

    # Canny边缘检测
    def btnByjc1(self):
        src = self.captured
        # if src is None:
        #     return

        blurred = cv.GaussianBlur(src, (3, 3), 0)
        gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

        grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
        grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

        dst = cv.Canny(grad_x, grad_y, 30, 150)
        self.ret=dst
        # dst = cv.Canny(gray, 50, 150)

    def btnSave3_Clicked(self):
        if not hasattr(self, "captured"):
            return
        cv.imwrite('byjc.jpg',self.ret)
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
        cv.imwrite('suofang.jpg',self.suofang)
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
        cv.imwrite('cut.jpg',self.cut)
        print('保存成功')



    def btnThreshold_Clicked(self):
        '''
        Otsu自动阈值分割
        '''
        if not hasattr(self, "captured"):
            return

        _, self.cpatured = cv.threshold(
            self.cpatured, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec())
