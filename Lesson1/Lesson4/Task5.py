'''На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, 
от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?'''

from scipy import stats
import numpy as np

d = 25
x = 190
m = 178
d = np.sqrt(d)
print((x - m) / d)

