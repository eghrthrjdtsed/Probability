'''В университет на факультеты A и B поступило равное количество студентов, а на факультет 
C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A 
сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента 
факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A 
б). на факультете B в). на факультете C?'''

import numpy as np

def probadility_general(k, n, p):
    return k / n * p

def probadility_of_each(k, n, p):
    P = result
    return (k / n * p) / P

p1 = probadility_general(1, 4, 0.8)
p2 = probadility_general(1, 4, 0.7)
p3 = probadility_general(1, 2, 0.9)
result = p1 + p2 + p3
print(f"Probability general: {result:.3f}") #Общая

first_athlete = probadility_of_each(1, 4, 0.8) #Вероятность студента факультета А
print(f"First athlete: {first_athlete:.9f}")

second_athlete = probadility_of_each(1, 4, 0.7) #Вероятность студента факультета В
print(f"Second athlete: {second_athlete:.9f}")

third_athlete = probadility_of_each(1, 2, 0.9) #Вероятность студента факультета С
print(f"Third athlete: {third_athlete:.9f}")