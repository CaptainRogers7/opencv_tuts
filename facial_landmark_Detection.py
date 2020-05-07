# -*- coding: utf-8 -*-
"""
Created on Fri May  8 03:42:56 2020

@author: pushk
"""

import cv2 as cv
import dlib
from imutils import face_utils

path='shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(path)

cap = cv.VideoCapture(0)
while(True):
    _,frame=cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #detect faces in gray scale image
    #The first parameter to the detector  is our grayscale image 
    #The second parameter is the number of image pyramid layers to apply when upscaling the image prior to applying the detector 
    rects = detector(gray, 0)
    
    # For each detected face, find the landmark.
    for (i, rect) in enumerate(rects):
        
        shape = predictor(gray, rect)# Make the prediction and transfom it to numpy array
        shape = face_utils.shape_to_np(shape)
    
        # Draw on our image, all the finded cordinate points (x,y) 
        for (x, y) in shape:
            cv.circle(frame, (x, y), 2, (0, 255, 0), -1)
    cv.imshow("Output", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()
cap.release()
    