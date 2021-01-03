import cv2
import numpy as np

img = cv2.imread('Resources/group.jpg')
kernel = np.ones((5, 5), np.uint8)

if img is not None:

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to Gray Image
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # Make Blur Image
    imgCanny = cv2.Canny(img, 150, 200)  # To Detect the Edge of Image, If threshold Increases then edge is low
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)  # If Iteration increases, thickness will increase
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)  # Opposite of Dilation

    imgGrayShow = cv2.resize(imgGray, (960, 540))
    imgBlurShow = cv2.resize(imgGray, (960, 540))
    imgCannyShow = cv2.resize(imgCanny, (960, 540))
    imgDilationShow = cv2.resize(imgDilation, (960, 540))
    imgErodedShow = cv2.resize(imgEroded, (960, 540))

    cv2.imshow("Gray Image", imgGrayShow)
    cv2.imshow("Blur Image", imgBlurShow)
    cv2.imshow("Canny Image", imgCannyShow)
    cv2.imshow("Dilation Image", imgDilationShow)
    cv2.imshow("Eroded Image", imgErodedShow)

    cv2.waitKey(0)
else:
    print("Image is not available")
