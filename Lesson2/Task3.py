'''Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?'''

import numpy as np
from math import factorial


def probadility(n, k):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) 
       
def probability_heads(p, n, k):
    C_kn = probadility(n, k)
    return C_kn * (p**k) * (1 - p)**(n - k)

probadility(144, 70)
result = probability_heads(0.5, 144, 70)
print(f"Probability heads:{result:.3f}")