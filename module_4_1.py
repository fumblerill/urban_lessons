from fake_math import divide as df
from true_math import divide as dt

numbers=[]
numbers.extend(input('Введите числа, в виде x, y: '))
numbers = [int(char) for char in numbers if char.isdigit()]

print(f'Фейковая математика говорит {df(*numbers)}')
print(f'Настоящая математика говорит {dt(*numbers)}')