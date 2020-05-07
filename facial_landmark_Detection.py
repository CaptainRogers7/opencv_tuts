# -*- coding: utf-8 -*-
"""
Created on Fri May  8 03:42:56 2020

@author: pushk
"""

import cv2 as cv
import dlib

cap = cv.VideoCapture(0)
while(True):
    _,frame=cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # show the gray image
    cv.imshow("Output", gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()
cap.release()
    