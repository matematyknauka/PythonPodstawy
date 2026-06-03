from numba import njit
import numpy as np

@njit
def algorytm(macierz_bgr, macierz_hsv, h_min, h_max, s_min, s_max, v_min, v_max, wiersze, kolumny):

    wynik = np.zeros((wiersze, kolumny, 3), dtype = np.uint8)

    for x in range(wiersze):
        for y in range(kolumny):

            h = macierz_hsv[x, y, 0]
            s = macierz_hsv[x, y, 1]
            v = macierz_hsv[x, y, 2]
            if h_min <= h <= h_max and s_min <= s <= s_max and v_min <= v <= v_max:
                wynik[x, y] = [0, 0, 0]

            else:
                wynik[x, y] = macierz_bgr[x, y]
    return wynik
                


        

    