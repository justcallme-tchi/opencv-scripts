# OpenCV Basics - Computer Vision Learning Scripts

A comprehensive collection of Python scripts for learning OpenCV and computer vision fundamentals. Perfect for beginners getting started with image processing, transformations, and basic computer vision techniques.

## 🎯 Description

This repository contains well-commented Python scripts demonstrating essential OpenCV functionalities:

- **Basic Operations**: Image loading, display, and basic manipulations
- **Drawing & Graphics**: Creating shapes, lines, and text on images
- **Image Transformations**: Scaling, rotation, translation, flipping, and cropping
- **Image Processing**: Blurring, edge detection, dilation, and erosion
- **Video Processing**: Video capture, frame processing, and real-time manipulation
- **Advanced Features**: Contour detection and face recognition

## 📁 Project Structure

```
opencv-basics/
├── images/                     # Sample images for testing
│   ├── Cat.jpg
│   ├── elder-man.jpg
│   ├── man.jpg
│   ├── squirrel.jpg
│   └── woman.jpg
├── videos/                     # Sample video files
│   ├── clip1.mp4
│   └── clip2.mp4
├── output/                     # Generated output images
│   ├── Cat_gray.jpg
│   ├── elder-man_cropped.jpg
│   ├── elder-man_flipped-horizontal.jpg
│   ├── elder-man_resized-500x500.jpg
│   ├── elder-man_rotated-45.jpg
│   ├── elder-man_rotated-90.jpg
│   └── elder-man_translated.jpg
├── basic_functions.py          # Core image processing operations
├── draw.py                     # Drawing shapes and text
├── image_transformations.py    # Geometric transformations
├── rescale_display.py          # Image/video scaling and display
├── identify_countours.py       # Contour detection (in development)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Setup and Installation

### Prerequisites
- **Python 3.7+** (recommended: Python 3.8 or higher)
- **pip** package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd opencv-basics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python -c "import cv2; print(cv2.__version__)"
   ```

## 🎮 Usage Examples

### Run Individual Scripts

```bash
# Basic image processing operations
python basic_functions.py

# Drawing shapes and text
python draw.py

# Image transformations (rotate, scale, translate)
python image_transformations.py

# Image and video rescaling
python rescale_display.py

# Contour detection
python identify_countours.py
```

### Key Features Demonstrated

**Basic Functions (`basic_functions.py`)**
- Gaussian blur for noise reduction
- Canny edge detection
- Morphological operations (dilation/erosion)
- Image resizing and cropping

**Drawing Operations (`draw.py`)**
- Creating blank canvases
- Drawing rectangles, circles, and lines
- Adding text with different fonts
- Color manipulation (BGR format)

**Image Transformations (`image_transformations.py`)**
- Translation (shifting images)
- Rotation around custom points
- Scaling with different interpolation methods
- Horizontal/vertical flipping
- Cropping specific regions

**Video Processing (`rescale_display.py`)**
- Video file reading and display
- Real-time frame processing
- Resolution changing for live video
- Frame-by-frame manipulation

## 📚 Learning Path

1. **Start with `draw.py`** - Learn basic OpenCV window management and drawing
2. **Move to `basic_functions.py`** - Understand core image processing operations
3. **Explore `rescale_display.py`** - Work with images and videos at different scales
4. **Try `image_transformations.py`** - Master geometric transformations
5. **Experiment with `identify_countours.py`** - Advanced shape detection

## 🛠 Dependencies

- **opencv-contrib-python** - Complete OpenCV package with extra modules
- **numpy** - Numerical operations and array handling
- **caer** - Additional computer vision utilities
- **matplotlib** - For advanced plotting and visualization
- **imutils** - Convenience functions for common OpenCV operations

## 💡 Tips for Beginners

- Press any key to close image windows when using `cv.waitKey(0)`
- Press 'd' to exit video playback loops
- Images are stored as NumPy arrays in BGR format (Blue, Green, Red)
- Coordinate system: (0,0) is top-left corner
- Always check if images loaded successfully before processing

## 🔄 Common Operations Reference

```python
# Load image
img = cv.imread('path/to/image.jpg')

# Display image
cv.imshow('Window Name', img)

# Wait for keypress
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()

# Save image
cv.imwrite('output/image.jpg', processed_img)
```

## 🤝 Contributing

Feel free to add more examples, improve documentation, or suggest enhancements. This project is designed for learning, so clarity and educational value are priorities.

## 📝 Notes

- All output images are automatically saved to the `output/` folder
- Sample images and videos are included for immediate testing
- Scripts include detailed comments explaining each operation
- Error handling is implemented for file loading operations

---

**Happy Learning!** 🎉 Start with any script that interests you and experiment with different parameters to see how they affect the results