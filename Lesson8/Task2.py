'''Измерены значения IQ выборки студентов,
обучающихся в местных технических вузах:
131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
Известно, что в генеральной совокупности IQ распределен нормально.
Найдите доверительный интервал для математического ожидания с надежностью 0.95.'''

import numpy as np
import scipy.stats as st
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

alpha = 0.05
n = len(iq)
mean = iq.mean()
print(f"mean: {mean}")

sigma = iq.std(ddof=1)
print(f"sigma: {sigma}")

t = st.t.ppf(alpha / 2, df = n - 1)
print(f"critical t: {t}")

x1 = mean + t * sigma / np.sqrt(n)
x2 = mean - t * sigma / np.sqrt(n)
print(f"range: {x1} : {x2}")


#Доверительный интервал от 110.55 - 125.64 с 0.95 долей вероятности захватывает математическое ожидание 
