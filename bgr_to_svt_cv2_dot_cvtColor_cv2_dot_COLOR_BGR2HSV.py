import numpy as np
import cv2

bgr = cv2.imread("portret.jpg")
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

# print(hsv)

# Dodatkowo zapis na dysku

cv2.imwrite("zdjecie_hsv.jpg", hsv)