# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

from scipy import stats
import numpy as np


a = 1 - stats.norm.cdf(182, loc = 174, scale = 8)
print(f"a): {a}")

b = 1 - stats.norm.cdf(190, loc = 174, scale = 8)
print(f"b): {b}")

v = stats.norm.cdf(190, loc = 174, scale = 8) - stats.norm.cdf(166, loc = 174, scale = 8)
print(f"v): {v}")

g = stats.norm.cdf(182, loc = 174, scale = 8) - stats.norm.cdf(166, loc = 174, scale = 8)
print(f"g): {g}")

d = stats.norm.cdf(190, loc = 174, scale = 8) - stats.norm.cdf(158, loc = 174, scale = 8)
print(f"d): {d}")

e = 1 -  stats.norm.cdf(190, loc = 174, scale = 8)  + stats.norm.cdf(150, loc = 174, scale = 8)
print(f"e): {e}")

y = 1 -  stats.norm.cdf(198, loc = 174, scale = 8)  + stats.norm.cdf(150, loc = 174, scale = 8) 
print(f"y): {y}")

j =  stats.norm.cdf(166, loc = 174, scale = 8) 
print(f"j): {j}")



