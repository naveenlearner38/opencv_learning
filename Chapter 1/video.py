import cv2

print('Imported')

# Video Show
cap = cv2.VideoCapture("Resources/video.mp4")

while True:
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (960, 540))
        cv2.imshow("Video Output", imgS)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
