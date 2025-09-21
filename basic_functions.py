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
edges = cv.Canny(blur, 100, 200)
cv.imshow('Edges', edges)

cv.waitKey(0)
cv.destroyAllWindows()