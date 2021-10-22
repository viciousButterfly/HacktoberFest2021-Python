import cv2

#reading image
my_img = cv2.imread("dog.jpg")

#converting BGR image to grayscale
gray_image = cv2.cvtColor(my_img,cv2.COLOR_RGB2GRAY)

#image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", my_img)
cv2.imshow("Pencil Sketch of Dog", pencil_sketch)
cv2.waitKey(0)