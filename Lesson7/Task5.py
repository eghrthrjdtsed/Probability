'''Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить
данную гипотезу, если известно, что размеры изделий подчинены нормальному закону
распределения. Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34'''


import numpy as np
from scipy import stats


def testing_the_hypothesis(mu, x_mean, x_len, x_sigma):
    return (x_mean - mu) / (x_sigma / np.sqrt(x_len))


x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
mu = 2.5
alpha = 0.05
x_len = len(x)
x_mean = np.mean(x)
x_sigma = x.std(ddof=1)
t = stats.t.ppf(1 - alpha / 2, df=x_len - 1)
result = testing_the_hypothesis(mu, x_mean, x_len, x_sigma)
print(f"Observable: {result}")
print(f"critical t: {t}")

# t не принадлежит критической области, гипотеза H0 не отвергается на уровне значимости 0.05

