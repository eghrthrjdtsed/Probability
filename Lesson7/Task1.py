'''Даны две независимые выборки. Не соблюдается условие нормальности
x1 380,420, 290
y1 140,360,200,900
Сделайте вывод по результатам, полученным с помощью функции, имеются ли статистические различия между группами?'''

import numpy as np
import scipy.stats as stats

x = np.array([380,420, 290])
y = np.array([140,360,200,900])

print(stats.mannwhitneyu(x, y))

#pvalue 0.62 > alpha 0.05 -> H0 не отвергается, различий нет.
