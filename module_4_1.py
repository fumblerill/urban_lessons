from fake_math import divide as df
from true_math import divide as dt

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

print(f'Фейковая математика говорит {df(x, y)}')
print(f'Настоящая математика говорит {dt(x, y)}')