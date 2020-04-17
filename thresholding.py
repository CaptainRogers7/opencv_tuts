# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:13:12 2020

@author: pushk
"""

import cv2
path="E:\pyimageSearch\grad.jpg"
img = cv2.imread(path,0)

#use thresholding techniques

#binary thresholding
_, th1= cv2.threshold(img,127,255,cv2.THRESH_BINARY)#source,threshold range,threshold type
# we compare the pixel values of the image with the threshold value 127. If the value is <127 we assign it 0
#else 255

#thresholding binary inverse-opposite of binary threshold

_, th2= cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("image",img)
cv2.imshow("threshold image",th1)
cv2.imshow("threshold image",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()