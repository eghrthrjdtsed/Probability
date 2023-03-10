'''Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату 
(то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). 
Произвести расчет как с использованием intercept, так и без.'''


import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

x = zp.reshape(10, 1)
y = ks.reshape(10, 1)

model = LinearRegression()
# x = zp.reshape(-1, 1)
model.fit(x, y)
r_sq = model.score(x, y) #Коэффициент детерминации
print(f"R-squared: {r_sq}")

# x = sm.add_constant(x)
# model = sm.OLS(y, x)
# result = model.fit()
# print(result.summary())

const = model.intercept_ #Подбираем коэффициенты
beta = model.coef_[0]
print(f"intercept: {const}") #Выводим интерцепт
print(f"coef: {beta}") #Выводим коэффициент

x_x = np.hstack([np.ones((10, 1)), x])
print(x_x) #Матричный метод расчета коэффициентов линейной регрессии

b = np.dot(np.linalg.inv(np.dot(x_x.T, x_x)), x_x.T @ y)
print(b) #Так же выводим коэффициенты

# B1 = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp **2) - np.mean(zp) ** 2)
# print(f"B1: {B1}") #Выводим коэффициент

# B0 = np.mean(ks) - B1 * np.mean(zp)
# print(f"B0: {B0}") #Выводим интерцепт

'''Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).'''


# def mse_(B1, y, x, n = 10):
#     return np.sum((B1*x - y)**2) / n
# alpha = 1e-6
# B1 = 0.1
# n = 10
# for i in range(450):
#     B1 -= alpha * (2/n) * np.sum((B1 * x - y) * x) #mse
#     print('B1 = {}'.format(B1))
    
# print()
# B0 = 0.1
# for i in range(450):
#     B0 -= alpha * (2/n) * np.sum((B0 * x - y) * x)
#     print('B0 = {}'.format(B0))


plt.scatter(x, y)
plt.plot(x, beta * x + const, 'g' )
plt.title(f"r2 = {round(r_sq, 3)}")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# На 78.8 % зарплата влияет на значения крединого скоринга 