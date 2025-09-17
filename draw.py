import cv2 as cv
import numpy as np

# Option 1: Load an existing image from file
# img = cv.imread('images/Cat.jpg')
# cv.imshow('Cat', img)
# blank = np.zeros(img.shape, dtype='uint8')  
# ^ Creates a blank image with the same size as 'img' (useful to draw over existing pictures)

# Option 2: Create a brand new blank canvas (500x500 pixels, 3 channels for color)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint part of the image a certain color
# image[y1:y2, x1:x2] = (B, G, R)
blank[200:300, 300:400] = 0, 255, 0  # Green square
cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(image, start_point, end_point, color, thickness, lineType)
cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=2, lineType=cv.LINE_AA)
cv.imshow('Rectangle', blank)

# Filled rectangle (1/4 of the image size)
cv.rectangle(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 0, 0),
    thickness=cv.FILLED,
    lineType=cv.LINE_AA
)
cv.imshow('Filled Rectangle', blank)

# 3. Draw a circle
# cv.circle(image, center, radius, color, thickness, lineType)
cv.circle(
    blank,
    (blank.shape[1] // 2, blank.shape[0] // 2),  # center of image
    40,
    (0, 0, 255),  # red
    thickness=-1,
    lineType=cv.LINE_AA
)
cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(image, start_point, end_point, color, thickness, lineType)
cv.line(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 255, 255),  # white
    thickness=3,
    lineType=cv.LINE_AA
)
cv.imshow('Line', blank)

# 5. Write text
# cv.putText(image, text, origin, font, scale, color, thickness, lineType)
cv.putText(
    blank,
    'dayuuum',
    (0, 225),
    cv.FONT_HERSHEY_TRIPLEX,
    1.0,
    (127, 127, 127),  # gray
    2,
    lineType=cv.LINE_AA
)
cv.imshow('Text', blank)

# Wait indefinitely until a key is pressed, then close all windows
cv.waitKey(0)
cv.destroyAllWindows()
