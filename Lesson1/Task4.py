'''В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, 
что 2 приобретенных билета окажутся выигрышными?'''

import numpy as np
from math import factorial

def probability_win(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(n - k))) \
           / (np.math.factorial(n1) // (np.math.factorial(n1 - k1)))

result = probability_win(2, 2, 100, 2)
print(f"Probability win: {result:.5f}")