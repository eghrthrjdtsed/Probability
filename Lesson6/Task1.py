'''Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя 
M = 80, а объем выборки n = 256.'''

import numpy as np
from scipy import stats


n = 256
m = 80
alpha = 0.05  #1 - 0.95
sigma = 16
z = stats.norm.ppf(alpha / 2)
print(f"critical z: {z}")

x1 = m + z * sigma / np.sqrt(n)
x2 = m - z * sigma / np.sqrt(n)
print(f"range: {x1} : {x2}")

#Доверительный интервал от 78.04 - 81.96 с 0.95 долей вероятности захватывает математическое ожидание 