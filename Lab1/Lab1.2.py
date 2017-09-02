import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img_bgr = cv2.imread('input/image2.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_bgr_copy = img_bgr

xoi = math.ceil(img_bgr.shape[1] / 2)
yoi	= math.ceil(img_bgr.shape[0] / 2)

def roi(bgr,img, min, max):
	for i, row in enumerate(img):
		for j, dot in enumerate(row):
			if img[i][j] < min or img[i][j] > max :
				bgr[i][j] = [30 ,30, 30]

print('xoi : ' + str(xoi))
print('yoi : ' + str(yoi))
print('color of interest BGR : ' + str(img_bgr[xoi][yoi]))

cv2.line(img_bgr,(xoi-10,yoi),(xoi+10,yoi),(0,0,255),2)
cv2.line(img_bgr,(xoi,yoi-10),(xoi,yoi+10),(0,0,255),2)
cv2.circle(img_bgr,(xoi,yoi),3, (255,0,0), -1)
cv2.imshow('img_bgr with line',img_bgr)
cv2.imwrite('output/img_bgr_lab1_2.jpg',img_bgr)

img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
print('color of interest HSV : ' + str(img_hsv[xoi][yoi]))
cv2.imshow('img_hsv',img_hsv)
cv2.imwrite('output/img_hsv_lab1_2.jpg',img_hsv)

img_rgb = img_bgr[...,::-1]

#plt.imshow(img_gray,cmap='hsv')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

roi(img_bgr_copy,img_gray,0,150)
cv2.imshow('img_roi',img_bgr_copy)
cv2.imwrite('output/img_roi_lab1_2.jpg',img_bgr_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()