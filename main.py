import cv2

img = cv2.imread('Resources/group.jpg')

if img is not None:

    imgShow = cv2.resize(img, (960, 540))

    cv2.imshow("Image", imgShow)

    cv2.waitKey(0)

else:
    print("Image is not available")
