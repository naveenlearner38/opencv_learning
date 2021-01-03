import cv2
import numpy as np

img = cv2.imread('Resources/group.jpg')

if img is not None:

    imgHor = np.hstack((img, img))  # Horizontal stack
    imgVer = np.vstack((img, img))  # Vertical Stack

    imgHorShow = cv2.resize(imgHor, (960, 540))
    imgVerShow = cv2.resize(imgVer, (960, 540))

    cv2.imshow("Horizontal Image", imgHorShow)
    cv2.imshow("Vertical Image", imgVerShow)
    cv2.waitKey(0)

else:
    print("Image is not available")
