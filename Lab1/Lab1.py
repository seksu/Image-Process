import cv2
import numpy as np
import math

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

bitDepth = 6

def plotSurface(img):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	x, y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
	z = img[0:img.shape[0]][0:img.shape[1]]
	surf = ax.plot_surface(x, y, z, cmap=cm.hsv)
	plt.show()
	plt.pause(.001)

def quantization(img, depth):
	maxValue    = 256
	minValue    = 0
	qLevel 		= 2**depth

	qStep 		= (maxValue - minValue)/qLevel

	for i, row in enumerate(img):
		for j, dot in enumerate(row):
			img[i][j] = math.floor(img[i][j] / qStep)

def levelCovert(img, depth):
	maxValue = 255 
	qLevel 		= 2**depth
	for i, row in enumerate(img):
		for j, dot in enumerate(row):
			img[i][j] = (img[i][j] * maxValue) / qLevel

rgb = cv2.imread('input/image1.jpg')

gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
grayCopy = gray

cv2.imshow('rgb',rgb)
cv2.imwrite('output/rgb.jpg',rgb)
cv2.imshow('gray',gray) 
cv2.imwrite('output/gray.jpg',gray)

print('RGB Shape is : ' + str(rgb.shape))
print('RGB Size is  : ' + str(rgb.size))
print('RGB Type is  : ' + str(rgb.dtype))

im_color = cv2.applyColorMap(gray, cv2.COLORMAP_HOT) 	# for color map
cv2.imshow('colormap',im_color)
cv2.imwrite('output/colormap.jpg',im_color)

quantization(gray,bitDepth)								# for quantize
cv2.imshow('quantize',gray)
cv2.imwrite('output/quantize(' + str(2**bitDepth) + ').jpg',gray)

im_color = cv2.applyColorMap(gray, cv2.COLORMAP_HOT) 	# for color map
cv2.imshow('colormapQu',im_color)
cv2.imwrite('output/colormap(' + str(2**bitDepth) + ').jpg',im_color)

levelCovert(gray,bitDepth)								# for quantize in 256 level
cv2.imshow('quantizeLevelCovert',gray)
cv2.imwrite('output/quantize(256).jpg',gray)

plotSurface(grayCopy)

cv2.waitKey(0)
cv2.destroyAllWindows()

