'''Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в 
первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, 
что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы 
одна деталь г). от одной до двух деталей?'''

import numpy as np

def probadility_general(k, n, p):
    return k / n * p

def probadility_of_each(k, n, p):
    P = result
    return (k / n * p) / P

def probadility_one_detail():
    P = result
    return 1 - P

p1 = probadility_general(1, 3, 0.1)
p2 = probadility_general(1, 3, 0.2)
p3 = probadility_general(1, 3, 0.25)
result = p1 + p2 + p3
print(f"Probability general: {result:.3f}") #Вероятность поломки всех деталей

res = probadility_one_detail()
print(f"Probability one detail: {res:.3f}") #Вероятность поломки хотя бы одной детали
