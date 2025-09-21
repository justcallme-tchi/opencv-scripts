import cv2 as cv 
import numpy as np

# ------------------------------------------------
# Load the image
# ------------------------------------------------
Image = cv.imread('images/elder-man.jpg')

if Image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# ------------------------------------------------
# Utility Functions
# ------------------------------------------------
def rescaleFrame(frame, scale=0.15):
    """
    Rescales an image by a given scale factor.
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def translate(image, x, y):
    """
    Shifts an image along the x and y axes.
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    """
    Rotates an image around a point (default = image center).
    """
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w // 2, h // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, (w, h))

# ------------------------------------------------
# Apply Transformations
# ------------------------------------------------

# 1. Translation
translated = translate(Image, 100, 100)
cv.imshow('Translated', rescaleFrame(translated))
cv.imwrite("Output/elder-man_translated.jpg", translated)

# 2. Rotation
rotated = rotate(Image, -45)
cv.imshow('Rotated (-45%)', rescaleFrame(rotated))
cv.imwrite("Output/elder-man_rotated-45.jpg", rotated)

rotated_twice = rotate(rotated, -90)
cv.imshow('Rotated Again (-90%)', rescaleFrame(rotated_twice))
cv.imwrite("Output/elder-man_rotated-90.jpg", rotated_twice)

# 3. Resizing
resized = cv.resize(Image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized (500x500)', resized)
cv.imwrite("Output/elder-man_resized-500x500.jpg", resized)

# 4. Flipping
flipped = cv.flip(Image, 1)
cv.imshow('Flipped (horizontal)', rescaleFrame(flipped))
cv.imwrite("Output/elder-man_flipped-horizontal.jpg", flipped)

# 5. Cropping
cropped = Image[200:400, 300:400]
cv.imshow('Cropped', rescaleFrame(cropped))
cv.imwrite("Output/elder-man_cropped.jpg", cropped)

# ------------------------------------------------
# Exit
# ------------------------------------------------
cv.waitKey(0)
cv.destroyAllWindows()
