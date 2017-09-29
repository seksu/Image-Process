import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc, 60.0, (600,400))

img1 = cv2.imread('input/image2.jpg')
img2 = cv2.imread('input/image3.jpg')

result_img = []

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

for i in range(1000):
	rate = i/1000 
	print(rate)
	result_img.append(cv2.addWeighted(img1,rate,img2,1-rate,0))

for i in range(1000):
	#cv2.imshow('result',result_img[i])
	out.write(result_img[i])
	#cv2.waitKey(1)

out.release()
cv2.waitKey(0)
cv2.destroyAllWindows()