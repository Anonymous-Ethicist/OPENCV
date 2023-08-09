import cv2 as cv 
'''img=cv.imread('photos/ron.jpg')
cv.imshow('RON',img)
cv.waitKey(100)'''
capture=cv.VideoCapture('videos/hmm.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllwindows()  