'''Из колоды в 52 карты извлекаются случайным образом 4 карты. б) Найти вероятность, что среди
 4-х карт окажется хотя бы один туз.'''

# a)
import numpy as np
from math import factorial


def probability_ace(n, k, n1, k1):
    return 1- (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1))) 

result = probability_ace(48, 4, 52, 4) 

print(f"Probability ace: {result:.2f}")
