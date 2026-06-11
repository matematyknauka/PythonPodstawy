import cv2

"""
# Można odkomentować jeśli ktoś nie posiada zdjęć o równych wymiarach.
import numpy as np
macierz1 = np.full((1920, 1080, 3), 55, dtype = np.uint8)
macierz2 = np.full((1920, 1080, 3), 155, dtype = np.uint8)
cv2.imwrite("klatkaNr1.jpg", macierz1)
cv2.imwrite("klatkaNr2.jpg", macierz2)
"""


kl1_bgr = cv2.imread("klatkaNr1.jpg")
kl2_bgr = cv2.imread("klatkaNr2.jpg")

# Przygotowanie kodeka i "nagrywarki"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('film_bez_tla.mp4', fourcc, 0.5, (1080, 1920)) # szerokość, wysokość Liczba 0.5 to klatki na sekundę


out.write(kl1_bgr) # Dodanie klatki do filmu
out.write(kl2_bgr)

out.release() # Zwolnienie zasobów
