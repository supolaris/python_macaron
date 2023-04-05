import cv2
import numpy as np

img = cv2.imread('image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blue = cv2.medianBlur(gray, 5)

edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9,250,250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite('output_image.jpg', cartoon)
