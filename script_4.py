# ***********************************************
#   Name   : Mallawaarachchi M.R.I.G
#   Reg No : EG/2020/4066
#   Take Home Assignment 1
#   Question 4 - Block Averaging (Spatial Resolution Reduction)
# ***********************************************

import cv2
import numpy as np

# Load the image
img_path = 'data/original_image.jpg'
image = cv2.imread(img_path, cv2.IMREAD_COLOR)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {img_path}")

# Define block sizes 
block_sizes = [3, 5, 7]

# Function: Apply block averaging 
def block_average(img, block_size):
    h, w = img.shape[:2]
    output = np.copy(img)

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            y_end = min(y + block_size, h)
            x_end = min(x + block_size, w)
            block = img[y:y_end, x:x_end]
            mean_color = block.mean(axis=(0, 1), dtype=np.float32)
            output[y:y_end, x:x_end] = mean_color

    return output.astype(np.uint8)

# Process for each block size 
processed_results = [block_average(image, size) for size in block_sizes]

# Display original and processed images 
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image)

for i, result in enumerate(processed_results):
    win_name = f'Block Average {block_sizes[i]}x{block_sizes[i]}'
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win_name, 640, 480)
    cv2.imshow(win_name, result)

# Wait and cleanup 
cv2.waitKey(0)
cv2.destroyAllWindows()
