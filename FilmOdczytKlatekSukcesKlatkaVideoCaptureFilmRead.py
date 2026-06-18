import cv2

film = cv2.VideoCapture("film_testowy.mp4")

sukces, klatka = film.read()
i = 1

while sukces:
    print(f"klatka {i}")
    i = i + 1
    sukces, klatka = film.read()

film.release()