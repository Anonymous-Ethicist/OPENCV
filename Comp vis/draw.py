import cv2 as cv 
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)
'''img=cv.imread('photos/ron.jpg')
cv.imshow('Ron',img)'''

#painting in a certain colour
'''blank[200:300,300:400]=0,0,255
cv.imshow('Green',blank)'''

#drawing a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

#DRAWING  a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),80,(0,0,255),thickness=-1)
cv.imshow('circle',blank)

#draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('line',blank)

#writing text
cv.putText(blank,'Im goin to dl class ill clean balcony after that n then bathe',(20,20),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1.0,(255,255,255),2)
cv.imshow('TEXT',blank)
cv.waitKey(0)