import cv2 as cv
img=cv.imread('photos/ron.jpg')
cv.imshow('Ron',img)
#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BLUR
blur =cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT,)
cv.imshow('BLUR',blur)

#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny edges',canny)
#dilating the image
dilated=cv.dilate(canny,(9,9),iterations=6)
cv.imshow('Dilated',dilated)

#eroding
eroded=cv.erode(dilated,(9,9),iterations=6)
cv.imshow('Eroded',eroded)

#alternate way
resized=cv.resize(img,(1000,1200),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#CROPPING
cropped=img[50:200,200:400]
cv.imshow('CROPPED',cropped)
cv.waitKey(0)