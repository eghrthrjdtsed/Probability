'''Даны значения зарплат из выборки выпускников: 
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки 
дисперсий для данной выборки.'''


import numpy as np
from statistics import mean
import math



salary_values = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

average = salary_values.sum() / salary_values.size #среднее арифметическое
print(f"Average: {average:.0f}") 

average_sqrt = (np.sum((salary_values - average)**2) / salary_values.size)**0.5 #Cреднее квадратичное отклонение
print(f"Standard deviation: {average_sqrt}")

shifted_variance = np.sum((salary_values - average)**2) / salary_values.size #Cмещенная дисперсия
print(f"Shifted variance: {shifted_variance}")

not_shifted_variance = np.sum((salary_values - average)**2) / (salary_values.size - 1) #Не смещенная
print(f"Not_shifted_variance: {not_shifted_variance}")
