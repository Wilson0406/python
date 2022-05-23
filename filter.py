import cv2

image = cv2.imread(r"D:\Downloads\test1.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"D:\Downloads\My Projects\Python\test_grey.jpeg", gray_image)

inverted_image = 255 - gray_image
cv2.imwrite(r"D:\Downloads\My Projects\Python\test_inverted.jpeg", inverted_image)

blurred_image = cv2.GaussianBlur(inverted_image, (21,21),0)
cv2.imwrite(r"D:\Downloads\My Projects\Python\test_blurred.jpeg", blurred_image)

inverted_blurred = 255 - blurred_image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale = 256.0)
cv2.imwrite(r"D:\Downloads\My Projects\Python\test_sketch.jpeg", pencil_sketch)
