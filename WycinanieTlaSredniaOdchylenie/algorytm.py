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
    wartosc_srednia = srednia(macierz, wiersze, kolumny, kanal)
    for x in range(wiersze):
        for y in range(kolumny):
            suma_kwadratow_roznic = suma_kwadratow_roznic + (macierz[x, y, kanal] - wartosc_srednia) ** 2

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
def wytnij_tlo(macierz_zdjecia_bgr, macierz_zdjecia_hsv, wiersze_zdjecia, kolumny_zdjecia, h_min, h_max, s_min, s_max, v_min, v_max): # k to stala
    wynik = np.zeros((wiersze_zdjecia, kolumny_zdjecia, 3), dtype = np.uint8)
   
    
    for x in range(wiersze_zdjecia):
        for y in range(kolumny_zdjecia):
            h = macierz_zdjecia_hsv[x, y, 0]
            s = macierz_zdjecia_hsv[x, y, 1]
            v = macierz_zdjecia_hsv[x, y, 2]
            
            # Warunek rozbity na mniejsze linie dla lepszej czytelności
            if (h_min <= h <= h_max and 
                s_min <= s <= s_max and 
                v_min <= v <= v_max):
                
                wynik[x, y, 0 ] = 0
                wynik[x, y, 1 ] = 0
                wynik[x, y, 2 ] = 0
            else:
                wynik[x, y, 0] = macierz_zdjecia_bgr[x, y, 0]
                wynik[x, y, 1] = macierz_zdjecia_bgr[x, y, 1]
                wynik[x, y, 2] = macierz_zdjecia_bgr[x, y, 2]
                
    return wynik
                
            
# Uruchomienie algorytmu

k =  7

obraz_bgr = cv2.imread("portret.jpg")
obraz_hsv = cv2.cvtColor(obraz_bgr, cv2.COLOR_BGR2HSV)
wiersze_obrazu, kolumny_obrazu, _ = obraz_bgr.shape
tlo_bgr = cv2.imread("tlo.jpg")
tlo_hsv = cv2.cvtColor(tlo_bgr, cv2.COLOR_BGR2HSV)
tlo_wiersze, tlo_kolumny, _ = tlo_bgr.shape

h_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 0, k)
h_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 0, k)
s_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 1, k)
s_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 1, k)
v_min = zakres_min(tlo_hsv, tlo_wiersze, tlo_kolumny, 2, k)
v_max = zakres_max(tlo_hsv, tlo_wiersze, tlo_kolumny, 2, k)

cv2.imwrite("nowe.jpg", wytnij_tlo(obraz_bgr, obraz_hsv, wiersze_obrazu, kolumny_obrazu, h_min, h_max, s_min, s_max, v_min, v_max))
# Ostatni argument można modyfikować dla konkretnego zdjęcia. U mnie to 8.

            
            




   

    