import cv2
import numpy as np

img = cv2.imread('Resources/group.jpg')

if img is not None:

    imgShow = cv2.resize(img, (960, 540))

    width, height = 250,350

    # To Find the particular object from the Image

    pts1 = np.float32([[327, 301], [420, 291], [334, 436], [430, 425]]) # Points of the particular Object
    pts2 = np.float32([[0,0], [width, 0], [0,height], [width, height]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    imgOutput = cv2.warpPerspective(imgShow, matrix, (width, height) )

    cv2.imshow("Image", imgShow)
    cv2.imshow("Warp Image", imgOutput)

    cv2.waitKey(0)

else:
    print("Image is not available")
