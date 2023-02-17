'''Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность, 
что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?'''


import numpy as np
from math import factorial


def probadility(n, k):
    return (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))) 
       
def probability_burned(p, n, k):
    C_kn = probadility(n, k)
    return C_kn * (p**k) * (1 - p)**(n - k)

probadility(5000, 2)
result = probability_burned(0.0004, 5000, 2)
print(f"Probability burned:{result:.2f}")