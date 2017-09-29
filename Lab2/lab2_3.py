import cv2
import numpy as np
import math

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

img = cv2.imread('input/image4.jpg')

#cv2.imshow('img',img)

fig = plt.figure()
ax = fig.gca(projection='3d')
x = img[:,:,2]
y = img[:,:,1]
z = img[:,:,0]

ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

surf = ax.scatter(x, y, z, cmap=cm.hsv)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()