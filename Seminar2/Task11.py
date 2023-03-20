# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

number = int(input('Введите натуральное число больше 1: '))
fibonacci = 0
num1 = 0
num2 = 1
count = 1
while fibonacci < number: 
    fibonacci = num1 + num2
    num1 = num2
    num2 = fibonacci
    count += 1
if fibonacci == number:
    print(count)
else:
    print (-1)    





