import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2,2,1)
img=np.random.randint(0,255,(10,10))#生成0到255 的10*10矩阵
print(img[0,0])
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
x = img.shape[0]
y = img.shape[1]
ret = np.zeros(256)
for i in range(x):
	for j in range(y):
		ret[img[i][j]] += 1
a=[]
for i in range(256):
	a.append(i)

plt.bar(a,ret)

plt.subplot(2,2,3)
img1=np.random.randint(0,255,(10,10,3))#生成0到255 的10*10矩阵
plt.imshow(img1)

plt.subplot(2,2,4)
x = img1.shape[0]
y = img1.shape[1]
z=  img1.shape[2]
ret1 = np.zeros(256)
for i in range(x):
	for j in range(y):
		for k in range(z):
			ret1[img1[i,j,k]] += 1
plt.bar(a,ret1,color='r')
plt.show()
