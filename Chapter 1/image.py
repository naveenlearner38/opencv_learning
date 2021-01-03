import cv2

print('Imported')

# Image Show
img = cv2.imread("../Resources/group.jpg")
print(img)
if img is not None:
    imgS = cv2.resize(img, (960, 540))
    cv2.imshow("Output", imgS)
    cv2.waitKey(0)
else:
    print("Image is not available")
