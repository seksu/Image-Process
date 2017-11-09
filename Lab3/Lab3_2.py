import numpy as np
import cv2
from math import sqrt

img = cv2.imread('input/img2.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
high,width,_ = img.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out2.avi',fourcc, 2.0, (width,high))

def GaussianLowPass(input):
	M,N = input.shape
	tmp = [[0 for x in range(N)] for y in range(M)]
	#tmp = []
	for i, row in enumerate(input):
		for j, dot in enumerate(row):
			tmp[i][j] = sqrt(((i-M/2)**2)+((j-N/2)**2))
	return tmp

def GaussianHighPass(input,r,image):
	for i, row in enumerate(input):
		for j, dot in enumerate(row):
			input[i][j] = image[i][j]*(1-np.exp(-((input[i][j]**2)/2*(r**2))))
			#print(input[i][j])


ret,thresh = cv2.threshold(imgray,127,255,0)
img2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

M,N,_ = img.shape
img3 = [[0 for x in range(N)] for y in range(M)]
for i, row in enumerate(img3):
	for j, dot in enumerate(row):
		img3[i][j] = 255
img3 = np.asarray(img3).astype('uint8')
cv2.drawContours(img3, contours, 1, (0,255,0), 2)

cv2.imshow('im1',img3)
cv2.imshow('im2',img)

#//////////// filter and video ////////// 

#print(img3[0][0])

fft = np.fft.fft2(img3)

fftshift = np.fft.fftshift(fft)

#templet = GaussianLowPass(fftshift)
#GaussianHighPass(templet,15,fftshift)
#ifft = abs(np.fft.ifft2(templet)).astype('uint8')
#cv2.imshow('test3',ifft)

for i in range(0,10):
	templet = GaussianLowPass(fftshift)
	GaussianHighPass(templet,i,fftshift)
	ifft = abs(np.fft.ifft2(templet)).astype('uint8')
	cv2.imwrite("output/img2_"+str(i)+".jpg",ifft)

for im in range(0,10):
	temp = cv2.imread("output/img2_"+str(im)+".jpg")
	out.write(temp)

out.release()

cv2.waitKey(0)
cv2.destroyAllWindows()