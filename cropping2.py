import time

from PIL import Image
import cv2

img = Image.open("bird.jpg")
img2 = Image.open('boy.jpg')
photo = cv2.imread('bird.jpg')
photo2 = cv2.imread('boy.jpg')
cv2.imshow('Final', photo)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('Final', photo2)
cv2.waitKey()
cv2.destroyAllWindows()

face1 = img.crop((50, 100, 552, 630))
body1 = img.crop((50, 330, 575, 992))
face1.show()
time.sleep(2)

face2 = img2.crop((80, 50, 430, 350))
face2.show()
img2.paste(face1, (60, -200))
time.sleep(2)
img2.show()


body1.paste(face2, (10,0))
time.sleep(2)
body1.show()


