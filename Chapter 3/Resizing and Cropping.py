import cv2
import numpy as np

img = cv2.imread('Resources/group.jpg')

if img is not None:

    print(img.shape)  # To find size

    imgShow = cv2.resize(img, (960, 540))  # Resize ( width, height)
    imgCropped = img[0:200, 200:500]  # Crop (height, width)

    cv2.imshow("Image Resized", imgShow)

    cv2.imshow("Image Cropped", imgCropped)

    cv2.waitKey(0)

else:
    print("Image is not available")
