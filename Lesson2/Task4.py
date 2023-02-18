'''В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, 
из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова 
вероятность того, что все мячи белые? Какова вероятность того, что ровно два мяча белые? 
Какова вероятность того, что хотя бы один мяч белый?
'''

import numpy as np
from math import factorial


# все мячи белые
def probability_all_white(n, k, n1, k1):
    return (k / n) * ((k - 1) / (n - 1)) * (k1 / n1) * ((k1 - 1) / (n1 - 1)) 

# хотя бы один мяч белый
def probability_least_one_white1(n, k, n1, k1):
    return 1 - (k / n) * ((k - 1) / (n - 1)) * (k1 / n1) * ((k1 - 1) / (n1 - 1))

result1 = probability_all_white(10, 7, 11, 9)
result2 = probability_least_one_white1(10, 3, 11, 2) 

     


print(f"probability_all_white: {result1:.8f}")
print(f"probability_least_one_white1: {result2:.8f}")