def input_num(n):
    if (n >= 3) and (n < 21):
        return n
    else:
        print(f'Дурак, {n} не входит в диапозон от 3 до 20, вводи число снова')
        return input_num(int(input('Вводи число, только не косяч: ')))

result = []
n = input_num(int(input('Введите число от 3 до 20: ')))

for i in range(1, 21):
    for j in range(i+1, 21):
        if n % (i+j) == 0:
            result.append(str(i)+str(j))

print(f'Пароль для входа: {"".join(result)}')