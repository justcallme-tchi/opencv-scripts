# Converting image to grayscale
import cv2 as cv

# Show original image
img = cv.imread('images/Cat.jpg')
cv.imshow('Cat', img)

""" def convert_to_grayscale(image_path):
    # Read the image
    image = cv.imread(image_path)
    
    # Check if image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return None
    
    # Convert to grayscale
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    return gray_image

# Call the function
gray_image = convert_to_grayscale('images/Cat.jpg')

# Display the grayscale image
cv.imshow("Grayscale Image", gray_image)

# Save the grayscale image  
cv.imwrite("Output/Cat_gray.jpg", gray_image)
print(f"Image saved to Output/Cat_gray.jpg") """

#Blur image 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

#Edge Cascade
edges = cv.Canny(img, 125, 175) #reduce the number of found edges with passing the blured img instead
cv.imshow('Edges', edges)

#Dilating the image
dilated = cv.dilate(edges, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding the image
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#Resizeing the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping the image
cropped = img[50:200, 200:400] #consider img as a 2D array
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()