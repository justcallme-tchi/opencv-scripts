import cv2 as cv

# ------------------------------------------------
# Load and show the original image
# ------------------------------------------------
img = cv.imread('images/Cat.jpg')
cv.imshow('Original Cat', img)

# ------------------------------------------------
# Example function for grayscale conversion (optional)
# Uncomment if you want a reusable function
# ------------------------------------------------
"""
def convert_to_grayscale(image_path):
    # Read the image
    image = cv.imread(image_path)
    
    # Check if image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return None
    
    # Convert from BGR (default OpenCV format) to grayscale
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    return gray_image

# Call the function
gray_image = convert_to_grayscale('images/Cat.jpg')

# Display the grayscale image
cv.imshow("Grayscale Image", gray_image)

# Save the grayscale image to a folder called Output/
cv.imwrite("Output/Cat_gray.jpg", gray_image)
print(f"Image saved to Output/Cat_gray.jpg")
"""

# ------------------------------------------------
# Blur the image
# ------------------------------------------------
# cv.GaussianBlur(src, ksize, sigmaX, borderType)
# ksize = kernel size (must be odd numbers, e.g. (7,7))
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

# ------------------------------------------------
# Edge detection (Canny algorithm)
# ------------------------------------------------
# cv.Canny(image, threshold1, threshold2)
# Lower threshold = edges considered; higher threshold = edges kept
edges = cv.Canny(img, 125, 175)
# Better result: use blurred image to reduce noise
# edges = cv.Canny(blur, 125, 175)
cv.imshow('Edges', edges)

# ------------------------------------------------
# Dilate the edges (make lines thicker)
# ------------------------------------------------
# cv.dilate(src, kernel, iterations)
# kernel can be a tuple (e.g. (7,7)), iterations = how many times dilation is applied
dilated = cv.dilate(edges, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# ------------------------------------------------
# Erode the dilated edges (make lines thinner)
# ------------------------------------------------
# cv.erode(src, kernel, iterations)
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# ------------------------------------------------
# Resize the image
# ------------------------------------------------
# cv.resize(src, dsize, interpolation)
# interpolation:
# - INTER_AREA → shrinking
# - INTER_LINEAR / INTER_CUBIC → enlarging
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# ------------------------------------------------
# Crop the image
# ------------------------------------------------
# Images are arrays → img[y1:y2, x1:x2]
cropped = img[50:200, 200:400]  # height from 50→200, width from 200→400
cv.imshow('Cropped', cropped)

# ------------------------------------------------
# Wait for key press and close all windows
# ------------------------------------------------
cv.waitKey(0)
cv.destroyAllWindows()
