import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

path = "Resources/lena.png"
img = cv2.imread(path)

if img is not None:

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x+width, y+height), (255, 0, 0), 2)

    cv2.imshow("Image", img)

    cv2.waitKey(0)

else:
    print("Image is not available")
