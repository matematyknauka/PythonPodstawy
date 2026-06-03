import numpy as np
import cv2

def hsv_min_max(obraz):
    macierz_bgr = cv2.imread(obraz)
    macierz_hsv = cv2.cvtColor(macierz_bgr, cv2.COLOR_BGR2HSV)
    wiersze, kolumny, _ = macierz_hsv.shape
    
    h_min = macierz_hsv[0, 0, 0]
    s_min = macierz_hsv[0, 0, 1]
    v_min = macierz_hsv[0, 0, 2]
    
    h_max = macierz_hsv[0, 0, 0]
    s_max = macierz_hsv[0, 0, 1]
    v_max = macierz_hsv[0, 0, 2]
    
    for x in range(wiersze):
        for y in range(kolumny):
            h = macierz_hsv[x, y, 0]
            s = macierz_hsv[x, y, 1]
            v = macierz_hsv[x, y, 2]
            
            if h < h_min:
                h_min = h
                
            if s < s_min:
                s_min = s
                
            if v < v_min:
                v_min = v
                
            if h > h_max:
                h_max = h
                
            if s > s_max:
                s_max = s
                
            if v > v_max:
                v_max = v
                
    print(f"h od {h_min} do {h_max}, s od {s_min} do {s_max}, v od {v_min} do {v_max}")

hsv_min_max("wycinek.jpg")