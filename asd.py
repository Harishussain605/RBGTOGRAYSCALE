from tkinter import filedialog
import cv2

x = filedialog.askopenfilename()
print(x)

print("Converting")
image = cv2.imread(x)
#image = cv2.imread('haris vector.jpg')
cv2.imshow('Original', image)

cv2.waitKey()

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('newimage.png',gray_img)
cv2.imshow("grayscale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()



