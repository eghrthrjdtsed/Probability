'''Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна
99%? (Провести двусторонний тест.)'''

from scipy import stats
import numpy as np


def testing_the_hypothesis(x1, x_mean, n, std):
    return (x_mean - x1) / np.sqrt(std / n + std / n)

x1 = 200
x2 = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
x_mean = np.mean(x2)
std = np.var(x2, ddof=1)
n = len(x2)
alpha = 0.01
# d = np.sqrt(std)
t1 = stats.norm.ppf(alpha)
# t1 = stats.t.ppf(1 - alpha, df = n - 1)
result = testing_the_hypothesis(x1, x_mean, n, std)
print(f"Observable: {result}")
print(f"critical: {t1}")


