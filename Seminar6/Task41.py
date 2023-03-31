# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

import random
list_1 = [random.randint(0, 20) for _ in range(int(input('Введите количество элементов массива')))]
print(list_1)
count = 0
# for i in range(len(list_1)-1):
#     if list_1[i-1]< list_1[i] and list_1[i+1]<list_1[i]:
#         count += 1
# if list_1[len(list_1)-1]> list_1[len(list_1)-2] and list_1[len(list_1)-1]>list_1[0]:
#     count += 1
# print(count)   

for i in range(len(list_1)):
    print(list_1[(i-1)%len(list_1)], list_1[(i)%len(list_1)], list_1[(i+1)%len(list_1)])     