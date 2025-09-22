import cv2 as cv

img = cv.imread('images/squirrel.jpg') 
     
def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)   
    height = int(frame.shape[0] * scale)  
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img,0.1)
cv.imshow('Squirrel', img) 



cv.waitKey(0)
cv.destroyAllWindows()