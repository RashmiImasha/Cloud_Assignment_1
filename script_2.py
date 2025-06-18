# ***********************************************
#   Name   : Mallawaarachchi M.R.I.G
#   Reg No : EG/2020/4066
#   Take Home Assignment 1
#   Question 2 - Spatial Averaging
# ***********************************************

import cv2
import numpy as np

# Read the image 
img_path = 'data/original_image.jpg'
image = cv2.imread(img_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

# Define window names
window_names = ['Original Image', '3x3 Average', '10x10 Average', '20x20 Average']

# Create and resize all windows
for win in window_names:
    cv2.namedWindow(win, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win, 640, 480)

# Define averaging kernel sizes 
kernel_sizes = [(3, 3), (10, 10), (20, 20)]

# Show original image 
cv2.imshow(window_names[0], image)

# Apply and display blurred images 
for i, ksize in enumerate(kernel_sizes, start=1):
    blurred = cv2.blur(image, ksize)
    cv2.imshow(window_names[i], blurred)

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
