#test4-18.py：二值化阈值处理
import cv2
img=cv2.imread('chuyinx.jpg')
img1=img
img3=img
img4=img
# cv2.imshow('yt',img)
#
# img1[img1>127]=255
# img1[img1<=127]=0
# cv2.imshow('2',img1)
#
# ret,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)	#二值化阈值处理
# cv2.imshow('imgTHRESH_BINARY',img2)

img=cv2.imread('chuyinx.jpg')
cv2.imshow('img',img)


img3[img3>127]=255
img3[img3<127]=0
cv2.imshow('jd',img1)


t1,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print(t1)
cv2.imshow('imgTHRESH',img2)

for i in range(img4.shape[0]):
	for j in range(img4.shape[1]):
		for k in range(img4.shape[2]):
			if img4[i,j,k]>127:
				img4[i, j, k]=0
			else:
				img4[i, j, k] = 255

cv2.imshow('img for',img4)

cv2.waitKey(0)









