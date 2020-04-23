# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:56:46 2020

@author: pushk
"""

import cv2 
import numpy as np

image =cv2.imread("ronaldo.jpg",cv2.IMREAD_GRAYSCALE)

#find laplacian gradient of image
lap = cv2.Laplacian(image,cv2.CV_64F)#CV_64F is just datatype. and we are using a 64f due to negative slope induced by 
#transforming from white to black

#take the absolute value of our laplacian transformation and we are going to convert this value
#back to the unsigned 8 bit integer which is suitable for our output
lap=np.uint8(np.absolute(lap))
cv2.imshow("img",image)
cv2.imshow("laplacian",lap)

#SOBEL
sobelX= cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY= cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX=np.uint8(np.absolute(np.absolute(sobelX)))
sobelY=np.uint8(np.absolute(np.absolute(sobelY)))
cv2.imshow("img",image)
cv2.imshow("laplacian",lap)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)

cv2.waitKey(0)