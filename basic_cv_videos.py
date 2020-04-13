# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:58:59 2020

@author: pushk
"""

import cv2

#capturing live stream from camera

#creating object of class VideoCapture
cap = cv2.VideoCapture(0)
#for saving the video we use the videoWriter class and a fourcc code
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))#20-number of frames per second,(640,480)-size of capture

while(True):
    ret,frame= cap.read()  #if frame available ret will save true else false. the frame returned will be saved in frame variable
    if(ret==True):
        
        #if we want our frame to be in grayscale
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("grayframe",gray)
    
        #resding properties of frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        out.write(frame)#storing in output file
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release() #release capture variable
out.release()
cv2.destroyAllWindows()