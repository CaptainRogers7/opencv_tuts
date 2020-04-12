# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:57:04 2020

@author: pushk
"""

import cv2
import imutils

#reading image
image = cv2.imread("jp.jpg")
#dimesions
(h,w,d)=image.shape
#displaying image
cv2.imshow("Image", image)
cv2.waitKey(0)
# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]


#regions of interest
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

#resizing images
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

#resizing the pic while preserving aspect ratio using imutils
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

#rotating pic using imutils
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)
#rotating pic using imutils (avoid clipping)
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

#smoothing an image -we must blur an image to reduce high-frequency noise,
# making it easier for our algorithms to detect and understand the actual contents of the image rather than 
#just noise that will “confuse” our algorithms.
# Blurring an image is very easy in OpenCV and there are a number of ways to accomplish it
blurred = cv2.GaussianBlur(image, (11, 11), 0)#apply guassianblur with a 11 by 11 kernel for soothing
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


# draw a 2px thick red rectangle surrounding the face
#img : The destination image to draw upon. We’re drawing on output .
#pt1 : Our starting pixel coordinate which is the top-left. In our case, the top-left is (320, 60) .
#pt2 : The ending pixel — bottom-right. The bottom-right pixel is located at (420, 160) .
#color : BGR tuple. To represent red, I’ve supplied (0 , 0, 255) .
#thickness : Line thickness (a negative value will make a solid rectangle). I’ve supplied a thickness of 2 .
output = image.copy() #since drawing operations are performed inplace we take a copy
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

#The putText  function of OpenCV is responsible for drawing text on an image. Let’s take a look at the required parameters:
#img : The output image.
#text : The string of text we’d like to write/draw on the image.
#pt : The starting point for the text.
#font : I often use the cv2.FONT_HERSHEY_SIMPLEX . The available fonts are listed here.
#scale : Font size multiplier.
#color : Text color.
#thickness : The thickness of the stroke in pixels.

# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)