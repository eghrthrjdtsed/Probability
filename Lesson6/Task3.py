'''Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.'''

import numpy as np
from scipy import stats


a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
alpha = 0.05

a_mean = a.mean()
b_mean = b.mean()
print(f"daughters: {a_mean}, mothers: {b_mean}")

ab_len = len(a)

a_sigma = a.std(ddof=1)
b_sigma = b.std(ddof=1)
average_sigma = (a_sigma + b_sigma) / 2
print(f"sigma a: {a_sigma}, b: {b_sigma}")
print(f"average sigma: {average_sigma}")


se = np.sqrt(np.std(a, ddof=1)**2 / len(a) + np.std(b, ddof=1)**2 / len(b))
print(f"se {se}")

t = stats.t.ppf(1 - alpha / 2, df = 2 * (ab_len - 1))
print(f"critical t: {t}")

delta = b_mean - a_mean  
print(f"delta: {delta}")

ds1 = delta - t * se
ds = delta + t * se
print(ds1, ds) 

#Доверительный интервал от -6.26 - 10.06 с 0.95 долей вероятности захватывает математическое ожидание 
