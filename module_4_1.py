from fake_math import divide as df
from true_math import divide as dt

numbers = input('Введите числа, в виде x, y: ')
numbers = [int(num) for num in numbers.replace(',', ' ').split() if num.isdigit()]

print(f'Фейковая математика говорит {df(*numbers)}')
print(f'Настоящая математика говорит {dt(*numbers)}')