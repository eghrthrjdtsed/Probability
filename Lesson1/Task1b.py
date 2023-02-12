'''Из колоды в 52 карты извлекаются случайным образом 4 карты. б) Найти вероятность, что среди
 4-х карт окажется хотя бы один туз.'''

# a)
import numpy as np
from math import factorial


def probability_ace(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1))) / n


def probability_ace1(n, k): 
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k)) / n


p1 = probability_ace(4, 1, 48, 3) ; p2 = probability_ace(4, 2, 48, 2)

p3 = probability_ace(4, 3, 48, 1) ; p4 = probability_ace1(4, 4)

result = p1 + p2 + p3 + p4
print(f"Probability ace: {result:.2f}")
