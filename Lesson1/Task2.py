'''На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с
 цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. 
 Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
'''

import numpy as np
from math import factorial


p = 1 #Одна попытка

def probability_open(n, k):
    return 1 / (np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k)))

result = probability_open(10, 3)
print(f"Probability: {result:.3f}")