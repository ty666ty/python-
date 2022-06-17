import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import cv2 as cv

fig,axes=plt.subplots(2,2)#创建一个2行2列的画布
ax1=plt.subplot(2,2,1)
plt.subplot(2,2,1)
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.plot(x, y, marker="o")


ax2=plt.subplot(2,2,2)
x=np.linspace(-10,10,100)
y=1.5*x
plt.plot(x, y, marker="x")
plt.scatter(x,y)

ax3=plt.subplot(2,2,3)
x=np.linspace(-10,10,10)
y=np.cos(x)
plt.scatter(x,y)

ax4=plt.subplot(2,2,4)
x=np.linspace(-10,10,10)
y=np.cos(x)
plt.bar(x,y)


plt.show()