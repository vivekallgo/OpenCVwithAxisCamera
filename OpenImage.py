import numpy as np
import cv2

# Load an color image in grayscale
img1 = cv2.imread('axis_small.jpg',cv2.IMREAD_COLOR)

img2 = cv2.imread('axis_small.jpg',cv2.IMREAD_GRAYSCALE)

img3 = cv2.imread('axis_small.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow('Axis Color',img1)
cv2.imshow('Axis Gray',img2)
cv2.imshow('Axis No Change',img3)


cv2.waitKey(0)
cv2.destroyAllWindows()