import cv2
image = cv2.imread('haris vector.jpg')

cv2.imshow('Original', image)

cv2.waitKey()

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('haris2.png', gray_img)
cv2.imshow("new image grayscale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
