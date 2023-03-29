# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
import random
num = int(input('Введите количество элементов '))
marks = [random.randint(1, 10) for _ in range(num)]
print(marks)
minim = 11
maxim = 0
for i in range(len(marks)):
    if marks[i] > maxim:
        maxim = marks[i]
    elif marks[i] < minim:
        minim = marks[i]
for i in range(len(marks)):
    if marks[i] == minim:
        marks[i] = maxim
    elif marks[i] == maxim:
        marks[i] = minim
print(marks)          


