import cv2
import numpy as np



def showimg(image):
    cv2.imshow("View", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


img1 = cv2.imread("boy.jpg")
img2 = cv2.imread("bird.jpg")
showimg(img1)
showimg(img2)


# Cropping faces
face1 = img1[5:128, 70:190]
showimg(face1)
face2 = img2[30:180, 30:149]
showimg(face2)

# # Resizing faces
face2_resize = cv2.resize(face2, (120, 123))
showimg(face2_resize)
face1_resize = cv2.resize(face1, (119, 175))
showimg(face1_resize)



# Exchanging faces
img1[5:128, 70:190] = face2
showimg(img1)
img2[5:180, 30:149] = face1
showimg(img2)