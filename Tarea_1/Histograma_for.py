import numpy as np
import math

a = np.random.normal(0, 1, 1000)
bins = [-3, -2, -1, 0, 1, 2, 3]
for i in range(1, len(bins)):
    h = np.sum((a >= bins[i-1]) & (a < bins[i]))
    intervalo = f"{bins[i-1]:>4} a {bins[i]:>4}"
    barra = "#" * (h // 5)
    print(intervalo + " | " + barra)