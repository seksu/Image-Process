import cv2

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
import numpy as np

img = cv2.imread('input/image1.jpg',0)

fig = plt.figure()
ax = fig.gca(projection='3d')
x, y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
z = img[0:img.shape[0]][0:img.shape[1]]
surf = ax.plot_surface(x, y, z, cmap=cm.hsv)
plt.show()
plt.savefig('output/testplot.png')
