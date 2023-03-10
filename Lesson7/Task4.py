'''Даны 3 группы учеников плавания. Не соблюдается условие нормальности.
В 1 группе время на дистанцию 50 м составляют:
56, 60, 62, 55, 71, 67, 59, 58, 64, 67
Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
Есть
ли статистически значимые различия между группами?'''


import numpy as np
import scipy.stats as stats

a = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
b = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
c = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

print(stats.kruskal(a, b, c))

# pvalue=0.065 > alpha 0.05 H0 не отвергается, различий нет
