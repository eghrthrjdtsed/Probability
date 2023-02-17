'''Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
Стрелок выстрелил 100 раз. Найдите вероятность того, 
что стрелок попадет в цель ровно 85 раз.'''



import numpy as np
from math import factorial


def probadility(n, k):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) 
       
def probability_of_success(p, n, k):
    C_kn = probadility(n, k)
    return C_kn * (p**k) * (1 - p)**(n - k)

probadility(100, 85)
result = probability_of_success(0.8, 100, 85)
print(f"Probability of success:{result:.3f}")














