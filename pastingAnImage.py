from PIL import Image
import cv2
img = Image.open("mountain.jpg")
photo = cv2.imread('mountain.jpg')
cv2.imshow('Final', photo)
cv2.waitKey()
cv2.destroyAllWindows()

img2 = Image.open("sun.jpg")
img.paste(img2, (270, 60))
photo = cv2.imread("sun.jpg")
cv2.imshow('Final', photo)
cv2.waitKey()
cv2.destroyAllWindows()

img.save("pasted_picture.jpg")
photo = cv2.imread("pasted_picture.jpg")
cv2.imshow('Final', photo)
cv2.waitKey()
cv2.destroyAllWindows()
