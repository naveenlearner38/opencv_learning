import cv2
import numpy as np

print('Imported')

# Video Show
cap = cv2.VideoCapture(0)

# set the width and height, and UNSUCCESSFULLY set the exposure time
# For more info about cap.set() Visit below link:
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#cv2.VideoCapture.get

cap.set(3, 480)  # Width in px
cap.set(4, 480)  # Height in px
cap.set(10, 150)  # Brightness 0-100
cap.set(15, 0.1)  # Exposure time

myColors = [[135, 50, 149, 179, 255, 255], [135, 50, 149, 179, 255, 255]]  # Add Multiple Colors in this list

myColorValues = [[0, 0, 255], [0, 0, 255]]  # BGR - Write color value for above myColor

myPoints = []  # [x, y, colorId]


def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    newPoints = []

    for color in myColors:

        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)

        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)

    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, width, height = 0, 0, 0, 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, width, height = cv2.boundingRect(approx)

    return x + width // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (960, 540))
        imgResult = img.copy()
        newPoints = findColor(img, myColors)
        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)
        if len(myPoints) != 0:
            drawOnCanvas(myPoints, myColorValues)

        cv2.imshow("Video Output", imgResult)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
