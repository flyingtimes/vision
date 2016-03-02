# this is a sample program to use macbook camera and capture HoughLines from camera

import cv2
import numpy as np
import sys
import math

def processFrame(img):
	return img

def getLineFromImage(img):
	dst = cv2.Canny(img, 50, 200)
	cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
	if True: # HoughLinesP
	    lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 20, np.array([]), 30, 10)
	    if lines is not None:
			a,b,c = lines.shape
	    #for i in range(a):
	    #    cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

	else:    # HoughLines
	    lines = cv2.HoughLines(dst, 1, math.pi/180.0, 100, np.array([]), 0, 0)
	    a,b,c = lines.shape
	    for i in range(a):
	        rho = lines[i][0][0]
	        theta = lines[i][0][1]
	        a = math.cos(theta)
	        b = math.sin(theta)
	        x0, y0 = a*rho, b*rho
	        pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
	        pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
	        cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

	return cdst

capture = cv2.VideoCapture(0)
while True:
	ret, img = capture.read()
	#img=cv2.resize(img,(300,200))
	result = processFrame(img)
	results = getLineFromImage(result)
	cv2.imshow('some', results)
	if 0xFF & cv2.waitKey(5) == 27:
		break
cv2.destroyAllWindows()
