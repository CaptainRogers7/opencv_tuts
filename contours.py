# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:09:59 2020

@author: pushk
"""

import cv2
import numpy as np


img = cv2.imread("OpenCV_Logo.png")
#for better accuracy we generally use binary images to find contours
img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#contours is list containing all the contours of image

cv2.drawContours(img, contours, -1, (0,255,0), 3)# -1 means all contours. replace -1 with specific index for a specific contour
#3 is thickness of contours

cv2.imshow("image",img)
cv2.imshow("gray",img_gray)

cv2.waitKey(0)