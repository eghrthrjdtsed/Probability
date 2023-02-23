'''Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
Найдите ее среднее значение и дисперсию.'''
#M(x) = a + b / 2 Среднее значение
#D = (b - a)**2 / 12 Дисперсия

def find_average_value(a, b):
    return (b + a) / 2


def find_variance(a, b):
    return (b - a)**2 / 12


m = find_average_value(200, 800)
d = find_variance(200, 800)
print(f"The average value: {m}")
print(f"The variance: {d}")