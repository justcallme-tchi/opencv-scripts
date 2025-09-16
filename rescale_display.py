import cv2 as cv

# -----------------------------
# Load and Display an Image
# -----------------------------
img = cv.imread('images/Cat.jpg')  # Read image from file
cv.imshow('Cat', img)              # Show original image in a window

# -----------------------------
# Function: Rescale Frame (for images, videos, live video)
# -----------------------------
def rescaleFrame(frame, scale=0.75):
    """
    Rescales an image or video frame by a given scale factor.
    Works for images, recorded videos, and live video.
    """
    width = int(frame.shape[1] * scale)   # New width
    height = int(frame.shape[0] * scale)  # New height
    dimensions = (width, height)
    
    # Resize frame to new dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Example: Rescale the image
resized_image = rescaleFrame(img, scale=0.2)
cv.imshow('Resized Image', resized_image)

# Wait until a key is pressed before closing image windows
cv.waitKey(0)

# -----------------------------
# Function: Change Resolution (ONLY works for live video from camera)
# -----------------------------
def changeRes(width, height):
    """
    Changes the resolution of live video (camera capture).
    This does NOT work for images or pre-recorded videos.
    """
    capture.set(3, width)   # 3 → property ID for frame width
    capture.set(4, height)  # 4 → property ID for frame height

# -----------------------------
# Video Capture (file or webcam)
# -----------------------------
# Use '0' instead of filename for default camera
capture = cv.VideoCapture('videos/clip2.mp4')

while True:
    isTrue, frame = capture.read()  # Read one frame from the video
    
    if not isTrue:  # Break if video ends
        break
    
    # Rescale the frame
    frame_resized = rescaleFrame(frame, scale=0.2)
    
    # Display original and resized frames
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    # Exit loop when 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release video capture and close all windows
capture.release()
cv.destroyAllWindows()
