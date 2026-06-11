import cv2

film = cv2.VideoCapture("film_bez_tla.mp4")
szerokosc = film.get(cv2.CAP_PROP_FRAME_WIDTH)
print(szerokosc)

film.release()
