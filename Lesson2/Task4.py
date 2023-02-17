'''В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, 
из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова 
вероятность того, что все мячи белые? Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?
'''

import numpy as np
from math import factorial

def probability_color(n, k, n1, k1):
    return 1 - (np.math.factorial(n) // (np.math.factorial(n - k))) \
           / (np.math.factorial(n1) // (np.math.factorial(n1 - k1)))


def probability(n, k, n1, k1):
    return 1 - (np.math.factorial(n) // (np.math.factorial(n - k))) \
           / (np.math.factorial(n1) // (np.math.factorial(n1 - k1)))


res = probability(9, 2, 11, 2)
result = probability_color(7, 2, 10, 2)
print(f"Probability: {result:.2f}")
print(f"Probability: {res:.2f}")