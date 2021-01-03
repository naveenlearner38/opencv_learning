import cv2


def empty():
    pass


img = cv2.imread('Resources/group.jpg')

cv2.namedWindow("Trackbars")
cv2.resize("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)

if img is not None:

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    imgShow = cv2.resize(img, (960, 540))
    imgHSVShow = cv2.resize(imgHSV, (960, 540))

    cv2.imshow("Image", imgShow)
    cv2.imshow("HSV Image", imgHSVShow)

    cv2.waitKey(0)

else:
    print("Image is not available")
