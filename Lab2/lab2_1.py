import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import misc
from os import listdir

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc, 2.0, (490,368))

img = cv2.imread('input/image1.jpg',0)

scharr = np.array([[ -3, 0,  +3],
                   [-10, 0, +10],
                   [ -3, 0,  +3]])

sobelx = np.array([[ -1,-2,-1],
                   [  0, 0, 0],
                   [  1, 2, 1]])

sobely = np.array([[ -1, 0, 1],
                   [ -2, 0, 2],
                   [ -1, 0, 1]])

def change(img, step):
	for i,row in enumerate(img) :
		for j,col in enumerate(row) :
			if img[i][j] > step :
				img[i][j] = 0

grad = signal.convolve2d(img, scharr, boundary='symm', mode='same')
gx = signal.convolve2d(img, sobelx, boundary='symm', mode='same')
gy = signal.convolve2d(img, sobely, boundary='symm', mode='same')

powerx = np.power(gx, 2)
powery = np.power(gy, 2)
addxy  = np.add(powerx,powery)

gxy = np.sqrt(addxy).astype('uint8')
#print(gxy)

print("Gxy Min is : ", np.amin(gxy))
print("Gxy Max is : ", np.amax(gxy))
print("Gxy Avg is : ", np.mean(gxy))
print("Gxy Std is : ", np.std(gxy))

fig, (ax_orig, ax_mag) = plt.subplots(1,2)
ax_orig.imshow(img, cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()

ax_mag.imshow(gxy, cmap='gray')
ax_mag.set_title('Magnitude Gradius')
ax_mag.set_axis_off()

maxvalue = 255
stepvalue = int(255/10)

for i in range(10,0,-1):
	change(gxy,(i*stepvalue))
	cv2.imwrite("output/img_"+str(i)+".jpg",np.uint8(gxy))

imagesList = listdir("output/")

for im in range(0,10):
	temp = cv2.imread("output/img_"+str(im)+".jpg")
	out.write(temp)

out.release()

#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()