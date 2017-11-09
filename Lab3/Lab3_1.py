import cv2
import numpy as np
from math import sqrt

img = cv2.imread('input/img2.jpg',0)
high,width = img.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out1.avi',fourcc, 2.0, (width,high))

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
			input[i][j] = image[i][j]*(1-np.exp(-((input[i][j]**2)/(2*(r**2)))))
			#print(input[i][j])

cv2.imshow('img',img)

fft = np.fft.fft2(img)

fftshift = np.fft.fftshift(fft)

templet = GaussianLowPass(fftshift)
#templetArray = np.asarray(templet)
#cv2.imshow('templet',templetArray.astype('uint8'))
#GaussianHighPass(templet,100,fftshift)
#ifft = abs(np.fft.ifft2(templet)).astype('uint8')
#cv2.imshow("a",ifft)

for i in range(1,11):
 	templet = GaussianLowPass(fftshift)
 	#templetArray = np.asarray(templet)
 	#cv2.imshow('templet',templetArray.astype('uint8'))
 	GaussianHighPass(templet,i*10,fftshift)
 	ifft = abs(np.fft.ifft2(templet)).astype('uint8')
 	cv2.imwrite("output/img1_"+str(i)+".jpg",ifft)

# #cv2.imshow('img6',ifft)

for im in range(1,11):
	temp = cv2.imread("output/img1_"+str(11-im)+".jpg")
	out.write(temp)

out.release()

cv2.waitKey(0)
cv2.destroyAllWindows()