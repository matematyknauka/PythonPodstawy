import cv2

film = cv2.VideoCapture("film_bez_tla.mp4")
ilosc_klatek = film.get(cv2.CAP_PROP_FRAME_COUNT)
print(ilosc_klatek)

film.release()
