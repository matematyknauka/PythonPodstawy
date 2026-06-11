import cv2

film = cv2.VideoCapture("film_bez_tla.mp4")
wysokosc = film.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(wysokosc)

film.release()
