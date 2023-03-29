# Найдите сумму цифр трехзначного числа

number = int(input('Введите трехзначное число: '))
if number < 99 or number > 999:
    print('Вы ввели не трехзначное число')
else:
    sum1 = number % 10
    sum2 = number // 10 % 10
    sum3 = number // 100
    print (f'Сумма цифр введенного числа равна {sum1 + sum2 + sum3}')
