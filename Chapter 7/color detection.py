import cv2
import numpy as np


def empty(value):
    pass


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


img = cv2.imread('Resources/group.jpg')

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, empty)

if img is not None:

    while True:

        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        imgShow = cv2.resize(img, (960, 540))
        imgHSVShow = cv2.resize(imgHSV, (960, 540))

        h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
        h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
        s_min = cv2.getTrackbarPos("Saturation Min", "Trackbars")
        s_max = cv2.getTrackbarPos("Saturation Max", "Trackbars")
        v_min = cv2.getTrackbarPos("Value Min", "Trackbars")
        v_max = cv2.getTrackbarPos("Value Max", "Trackbars")
        # print(h_min, h_max, s_min, s_max, v_min, v_max)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        mask = cv2.inRange(imgHSV, lower, upper)

        maskShow = cv2.resize(mask, (960, 540))

        imageResult = cv2.bitwise_and(imgShow, imgShow, mask=maskShow)

        imgStack = stackImages(0.6, ([imgShow, imgHSVShow], [maskShow, imageResult]))
        # cv2.imshow("Image", imgShow)
        # cv2.imshow("HSV Image", imgHSVShow)
        # cv2.imshow("Mask", maskShow)
        # cv2.imshow("Mask", imageResult)
        cv2.imshow("Stack Image", imgStack)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else:
    print("Image is not available")
