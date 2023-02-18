'''В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, 
из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова 
вероятность того, что все мячи белые? Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?
'''

import numpy as np
from math import factorial



# все мячи белые
def probability_all_white(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1)))

# ровно два мяча белые
def probability_exactly_two_white(n, k, n1, k1):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1))) 
    
                 

# хотя бы один мяч белый
def probability_least_one_white(n, k, n1, k1):
    return 1 - (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) \
        / (np.math.factorial(n1) // (np.math.factorial(k1) * np.math.factorial(n1 - k1))) 


result1 = probability_all_white(16, 4, 21, 4)
result2 = probability_exactly_two_white(16, 2, 21, 4)
result3 = probability_least_one_white(16, 4, 21, 4)

print(f"probability_all_white: {result1:.4f}")
print(f"probability_exactly_two_white: {result2:.8f}")
print(f"probability_least_one_white: {result3:.4f}")