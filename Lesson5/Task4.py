'''Есть ли статистически значимые различия в росте
дочерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163'''

from scipy import stats
import numpy as np


x = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

x_mean = np.mean(x)
y_mean = np.mean(y)
x_v = np.var(x)
y_v = np.var(y)
x_l = len(x)
x.sort()
y.sort()
# y_l = y.shape
y_l = len(y)
t = stats.ttest_ind(x, y)
print(t)