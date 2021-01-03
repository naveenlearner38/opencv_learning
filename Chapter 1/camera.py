import cv2

print('Imported')

# Video Show
cap = cv2.VideoCapture(0)

# set the width and height, and UNSUCCESSFULLY set the exposure time
# For more info about cap.set() Visit below link:
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#cv2.VideoCapture.get

cap.set(3, 480)  # Width in px
cap.set(4, 480)  # Height in px
cap.set(10, 10)  # Brightness 0-100
cap.set(15, 0.1)  # Exposure time

while True:
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (960, 540))
        cv2.imshow("Video Output", imgS)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
