import cv2 as cv 
face = cv.CascadeClassifier('haar2.xml')
capture=cv.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    
    g=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    f=face.detectMultiScale(g,1.1,4)
    for (x,y,w,h) in f:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow('Video',frame)    
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()




