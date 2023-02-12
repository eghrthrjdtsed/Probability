'''В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом 
извлекает 3 детали. Какова вероятность того, 
что все извлеченные детали окрашены?'''

import numpy as np
from math import factorial

def probability_color(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(n - k))) \
           / (np.math.factorial(n1) // (np.math.factorial(n1 - k1)))

result = probability_color(9, 3, 15, 3)
print(f"Probability: {result:.2f}")