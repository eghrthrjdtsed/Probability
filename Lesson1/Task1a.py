'''Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, 
что все карты – крести. '''

# a)
import numpy as np
from math import factorial

def combinations_cross_card(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1)))

result = combinations_cross_card(13, 4, 52, 4)
print(f"Probability cross:{result:.4f}")



