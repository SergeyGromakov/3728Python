#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input('Введите количество элементов первого массива: '))
m = int(input('Введите количество элементов второго массива: '))
first_list = [random.randint(0, 10)for _ in range(n)]
second_list = [random.randint(0, 10) for _ in range(m)]
print(f'Первый массив чисел: {first_list}')
print(f'Второй массив чисел: {second_list}')
new_list = list((set(first_list)).intersection(set(second_list)))
print(f'Пересекающиеся значения: {new_list}')
for i in range(len(new_list)):
    min = new_list[i]
    for j in range(i+1, len(new_list)):
         if new_list[j] < min:
            min = new_list[j]
            new_list[i], new_list[j] = new_list[j], new_list[i]
print(f'Пересекающиеся значения в порядке увеличения: {new_list}')

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
#     lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
