# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:57:05 2020

@author: pushk
"""

import cv2
import numpy as np

def nothing(x):
    pass

#live tracking an object from real time video
cap=cv2.VideoCapture(0);

#finding mask parameters for blue color manually
    
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    #frame = cv2.imread("smarties.jpg")
    #for live tracking
    _, frame = cap.read()
    #for object detection convert image into hsv image
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
     
    #threshold the hsv image for a range of blue color
    
    #defining the upper and lower colour bound for the blue colour
    #l_b=np.array([110,50,50])
    #u_b=np.array([130,255,255])
    l_h=cv2.getTrackbarPos("LH","Tracking")
    l_s=cv2.getTrackbarPos("LS","Tracking")
    l_v=cv2.getTrackbarPos("LV","Tracking")
    
    u_h=cv2.getTrackbarPos("UH","Tracking")
    u_s=cv2.getTrackbarPos("US","Tracking")
    u_v=cv2.getTrackbarPos("UV","Tracking")
    
    l_b=np.array([l_h,l_v,l_s])
    u_b=np.array([u_h,u_s,u_v])
    #creating a mask and thresholding the hsv image for blue colour
    mask= cv2.inRange(hsv,l_b,u_b)
    #using bitwise and to mask the original image
    res = cv2.bitwise_and(frame, frame , mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()

cv2.destroyAllWindows()
