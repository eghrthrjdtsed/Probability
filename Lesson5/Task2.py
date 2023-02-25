'''Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
n=100 шариков средний диаметр
оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.'''

from scipy import stats
import numpy as np

def testing_the_hypothesis(x1, x2, n, std):
    return (x1 - x2) / np.sqrt(std / n + std / n)

x1 = 17.5
x2 = 17
n = 100
std = np.sqrt(4)
alpha = 0.05
t1 = stats.t.ppf(1 - alpha, df = n - 1)
result = testing_the_hypothesis(x1, x2, n, std)
print(f"Observable: {result}")
print(f"critical: {t1}")


