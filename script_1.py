# ***********************************************
#   Name   : Mallawaarachchi M.R.I.G
#   Reg No : EG/2020/4066
#   Take Home Assignment 1
#   Question 1
# ***********************************************

import cv2
import numpy as np

# Load the grayscale imag
img_path = 'data/original_image.jpg'
gray_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Create a resizable window
window_name = 'Intensity Adjustment Display'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# Define a Intensity control bar to adjust intensity
max_intensity = 8  
initial_intensity = 3  
current_intensity = initial_intensity

def apply_intensity_reduction(value):
    global current_intensity
    current_intensity = 2 ** (8-value)

    # Perform image compression
    img_reduced = np.uint8(np.floor(np.double(gray_image) / (current_intensity)))

    # Normalize the image
    updated_image = cv2.normalize(img_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    # Update the image intensity
    cv2.imshow(window_name, updated_image)

# Create a track bar
cv2.createTrackbar('Intensity', window_name, initial_intensity, max_intensity, apply_intensity_reduction)

# Show original image 
cv2.imshow(window_name, gray_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
