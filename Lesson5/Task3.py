'''Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна
99%? (Провести двусторонний тест.)'''

from scipy import stats
import numpy as np


def testing_the_hypothesis(mu, x_mean, n, sigma):
    return (x_mean - mu) / (sigma / np.sqrt(n))


mu = 200
alpha = 0.01
samples = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

x_mean = samples.mean()
print(x_mean)
sigma = samples.std(ddof=1)
print(sigma)

n = len(samples)
print(n)

t1 = stats.t.ppf(alpha / 2, df = n-1)
t2 = stats.t.ppf(1 - alpha / 2, df = n - 1)
print(f" t1 = {t1}, t2 = {t2}")

result = testing_the_hypothesis(mu, x_mean, n, sigma)
print(f"Observable: {result}")

# Критическая область (- inf, -3.25), (3.25, inf)
# t не принадлежит критической области, гипотеза H0 не отвергается на уровне значимости 0.01
# утверждение продавца верно, средний вес пачки действительно сосавляет 200г
