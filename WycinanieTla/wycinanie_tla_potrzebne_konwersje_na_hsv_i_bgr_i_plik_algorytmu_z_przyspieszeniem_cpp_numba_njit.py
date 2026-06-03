import numpy as np
import cv2
from wycinanie_tla_sam_algorytm_bez_operacji_dyskowych_numba_malpa_njit import algorytm

def wytnij_tlo(do_obrobki, h_min, h_max, s_min, s_max, v_min, v_max, wynik): #tolerancja jak się da to od min odjąć 10, do max dodać 10
    macierz_bgr = cv2.imread(do_obrobki)
    macierz_hsv = cv2.cvtColor(macierz_bgr, cv2.COLOR_BGR2HSV)
    wiersze, kolumny, _ = macierz_bgr.shape
    po_algorytmie = algorytm(macierz_bgr, macierz_hsv, h_min, h_max, s_min, s_max, v_min, v_max, wiersze, kolumny)
    cv2.imwrite(wynik, po_algorytmie)


wytnij_tlo("portret.jpg", 54, 85, 97, 255, 82, 152, "wynik.jpg") # po odejmowaniu powyższym
# Wartości unikatowe dla danego zdjęcia
    
    
    