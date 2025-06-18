# ***********************************************
#   Name   : Mallawaarachchi M.R.I.G
#   Reg No : EG/2020/4066
#   Take Home Assignment 1
#   Question 3 - Image Rotation (with size adjustment)
# ***********************************************

import cv2
import numpy as np
import math

# Load the original image 
img_path = 'data/original_image.jpg'
image = cv2.imread(img_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

# Get image dimensions 
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# Function to rotate with size adjustment 
def rotate_image(image, angle):
    # Compute rotation matrix
    rot_mat = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)

    # Compute the new bounding dimensions
    abs_cos = abs(rot_mat[0, 0])
    abs_sin = abs(rot_mat[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)

    # Adjust the rotation matrix to account for translation
    rot_mat[0, 2] += new_w / 2 - center[0]
    rot_mat[1, 2] += new_h / 2 - center[1]

    # Perform the actual rotation
    return cv2.warpAffine(image, rot_mat, (new_w, new_h))

# Perform the rotations 
rotated_45 = rotate_image(image, 45)
rotated_90 = rotate_image(image, 90)

# Define window names
window_names = ['Original Image', 'Rotated 45°', 'Rotated 90°']
images = [image, rotated_45, rotated_90]

# Create and show images
for name, img in zip(window_names, images):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 640, 480)
    cv2.imshow(name, img)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
