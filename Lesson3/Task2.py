'''В первом ящике находится 8 мячей, из которых 5 - белые. 
Во втором ящике - 12 мячей, из которых 5 белых. 
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
Какова вероятность того, что 3 мяча белые?'''


import numpy as np
from math import factorial


def probadility_white(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1)))
       

def probability_black(n, k, n1, k1):
    C_kn = probadility_white(n, k, n1, k1)
    return C_kn * (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1))) 

probadility_white(5, 2, 8, 2)
result = probability_black(5, 4, 12, 4)
print(f"Probability white: {result:.9f}")

probadility_white(3, 2, 8, 2)
res = probability_black(7, 4, 12, 4)
print(f"Probability black: {res:.9f}")

# p = p1 + p2

p = result + res
print(f"Probability_three_white: {p:.9f}")