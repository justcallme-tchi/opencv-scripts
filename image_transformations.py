import cv2 as cv 
import numpy as np

Image = cv.imread('images/elder-man.jpg')

# Check if the image was successfully loaded
if Image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Rescale function to resize images
def rescaleFrame(frame, scale=0.15):
    """
    Rescales an image by a given scale factor.
    Default scale is 0.15 (15% of original size) for much smaller display
    """
    width = int(frame.shape[1] * scale)   # New width
    height = int(frame.shape[0] * scale)  # New height
    dimensions = (width, height)
    
    # Resize frame to new dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Translation (shift Image along the x and  y axis)
def translate(Image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix , float32 takes a list with 2 lists inside of it
    dimensions = (Image.shape[1], Image.shape[0]) # 1 = width , 0 = height
    return cv.warpAffine(Image, transMat, dimensions) #warpAffine applies the transformation to the image

#how the shift works :
# -x --> left ,-y --> up 
# +x --> right, +y --> down

# Apply translation
translated = translate(Image, 100, 100)

# Rescale images to 15% of original size for much smaller display
rescaled_img = rescaleFrame(Image, scale=0.15)  
rescaled_translated = rescaleFrame(translated, scale=0.15)

# Display original and translated images (both rescaled to 15%)
cv.imshow('Original (15% size)', rescaled_img)
cv.imshow('Translated (15% size)', rescaled_translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w // 2, h // 2)

    # Perform the rotation
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, (w, h))

rotated = rotate(rescaled_img, 45)
cv.imshow('Rotated (45 degrees)', rotated)

# Wait for a key press (0 means wait indefinitely)
cv.waitKey(0)

# Close all windows when done
cv.destroyAllWindows()