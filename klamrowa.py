import numpy as np

x = np.arange(-10, 10, 0.1)
zakresy = [(x < -2) | (x > 2), (x >= -2) & (x <= 2)]
wartosci = [x**2, 2*x]

tab = np.select(zakresy, wartosci, 45)
print(tab)