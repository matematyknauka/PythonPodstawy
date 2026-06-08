from numba import njit
import cv2
import numpy as np

@njit
def srednia(macierz, wiersze, kolumny, kanal):
    suma = 0
    for x in range(wiersze):
        for y in range(kolumny):
            suma = suma + macierz[x, y, kanal]

    return suma / (wiersze * kolumny)

@njit
def odchylenie(macierz, wiersze, kolumny, kanal):
    suma_kwadratow_roznic = 0
    for x in range(wiersze):
        for y in range(kolumny):
            suma_kwadratow_roznic = suma_kwadratow_roznic + (macierz[x, y, kanal] - srednia(macierz, wiersze, kolumny, kanal)) ** 2

    return (suma_kwadratow_roznic / (wiersze * kolumny)) ** (1/2)

@njit
def zakres_min(macierz, wiersze, kolumny, kanal, k): # k to stała
    return max(0, int(srednia(macierz, wiersze, kolumny, kanal) - k * odchylenie(macierz, wiersze, kolumny, kanal)))

@njit
def zakres_max(macierz, wiersze, kolumny, kanal, k): # k to stała
    if k == 0:
        brzeg = 179
    else:
        brzeg = 255
    return min(brzeg, int(srednia(macierz, wiersze, kolumny, kanal) + k * odchylenie(macierz, wiersze, kolumny, kanal)))

@njit
def wytnij_tlo(macierz_zdjecia_bgr, macierz_zdjecia_hsv, wiersze_zdjecia, kolumny_zdjecia, macierz_tla_hsv, wiersze_tla, kolumny_tla, k): # k to stala
    wynik = np.zeros((wiersze_zdjecia, kolumny_zdjecia, 3), dtype = np.uint8)
    h_min = zakres_min(macierz_tla_hsv, wiersze_tla, kolumny_tla, 0, k)
    h_max = zakres_max(macierz_tla_hsv, wiersze_tla, kolumny_tla, 0, k)
    s_min = zakres_min(macierz_tla_hsv, wiersze_tla, kolumny_tla, 1, k)
    s_max = zakres_max(macierz_tla_hsv, wiersze_tla, kolumny_tla, 1, k)
    v_min = zakres_min(macierz_tla_hsv, wiersze_tla, kolumny_tla, 2, k)
    v_max = zakres_max(macierz_tla_hsv, wiersze_tla, kolumny_tla, 2, k)
    
    
    for x in range(wiersze_zdjecia):
        for y in range(kolumny_zdjecia):
            h = macierz_zdjecia_hsv[x, y, 0]
            s = macierz_zdjecia_hsv[x, y, 1]
            v = macierz_zdjecia_hsv[x, y, 2]
            
            # Warunek rozbity na mniejsze linie dla lepszej czytelności
            if (h_min <= h <= h_max and 
                s_min <= s <= s_max and 
                v_min <= v <= v_max):
                
                wynik[x, y] = [0, 0, 0]
            else:
                wynik[x, y] = macierz_zdjecia_bgr[x, y]
                
    return wynik
                
"""            
# Uruchomienie algorytmu

obraz_bgr = cv2.imread("portret.jpg")
obraz_hsv = cv2.cvtColor(obraz_bgr, cv2.COLOR_BGR2HSV)
wiersze_obrazu, kolumny_obrazu, _ = obraz_bgr.shape
tlo_bgr = cv2.imread("tlo.jpg")
tlo_hsv = cv2.cvtColor(tlo_bgr, cv2.COLOR_BGR2HSV)
tlo_wiersze, tlo_kolumny, _ = tlo_bgr.shape

cv2.imwrite("nowe.jpg", wytnij_tlo(obraz_bgr, obraz_hsv, wiersze_obrazu, kolumny_obrazu, tlo_hsv, tlo_wiersze, tlo_kolumny, 8))
# Ostatni argument można modyfikować dla konkretnego zdjęcia. U mnie to 8.
"""
            
            




   

    