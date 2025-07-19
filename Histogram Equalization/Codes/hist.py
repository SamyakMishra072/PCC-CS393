# Write a Python script to enhance the image used in the other question using simple Histogram Equalization technique. Also display the equalized histogram along with the enhanced image.


import cv2
import numpy
from matplotlib import pyplot as plt
inputImg = 'enh.jpg'
img = cv2.imread(inputImg)
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv,cv2.COLOR_YUV2BGR)
outputImg = 'result.jpg'
cv2.imwrite(outputImg, hist_equalization_result)
inputImg = 'result.jpg'
gray_img = cv2.imread(inputImg, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Result',gray_img)
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()
while True:
	k = cv2.waitKey(0) & 0xFF
	if k == 27: break
cv2.destroyAllWindows()
