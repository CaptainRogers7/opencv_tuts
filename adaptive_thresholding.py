# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:40:44 2020

@author: pushk
"""

import cv2 

img = cv2.imread('sudoku.jpg',0)

_, th1=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11, 2);

cv2.imshow("IMAGE",img)

cv2.imshow("threshold",th1)

cv2.imshow("AD_threshold",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()