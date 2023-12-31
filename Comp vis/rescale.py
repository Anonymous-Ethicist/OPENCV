import cv2 as cv 
img=cv.imread('photos/ron.jpg')
cv.imshow('ron',img)
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

'''cv.waitKey(0)'''
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('videos/hmm.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
#alternate way
resized=cv.resize(img,(400,200))
cv.imshow('resized',resized)

cv.destroyAllwindows()  