import cv2

from algorytm import zakres_min, zakres_max, wytnij_tlo
k = 2 #k można modyfikować.
tlo_bgr = cv2.imread("tlo.jpg")
tlo_wiersze, tlo_kolumny, _ = tlo_bgr.shape
tlo_hsv = cv2.cvtColor(tlo_bgr, cv2.COLOR_BGR2HSV)
h_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 0, k)
h_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 0, k)
s_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 1, k)
s_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 1, k)
v_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 2, k)
v_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 2, k)




film = cv2.VideoCapture("film_testowy.mp4")
film_klatki_na_sekunde = film.get(cv2.CAP_PROP_FPS)
film_szerokosc_klatki = int(film.get(cv2.CAP_PROP_FRAME_WIDTH))
film_wysokosc_klatki = int(film.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
film_rezultat = cv2.VideoWriter("wynik.mp4", fourcc, film_klatki_na_sekunde, (film_szerokosc_klatki, film_wysokosc_klatki))

sukces, klatka_bgr = film.read()
while sukces:
    klatka_hsv = cv2.cvtColor(klatka_bgr, cv2.COLOR_BGR2HSV)
    wiersze_klatki, kolumny_klatki, _ = klatka_bgr.shape
    film_rezultat.write(wytnij_tlo(klatka_bgr, klatka_hsv, wiersze_klatki, kolumny_klatki, h_min, h_max, s_min, s_max, v_min, v_max))
    sukces, klatka_bgr = film.read()

film.release()
film_rezultat.release()