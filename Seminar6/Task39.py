# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random
list_1=[random.randint(0, 10) for _ in range(int(input('Введите количество элементов первого массива: ')))]
list_2=[random.randint(0, 10) for _ in range(int(input('Введите количество элементов второго массива: ')))]
print(f'Первый массив {list_1}')
print(f'Второй массив {list_2}')
list_3 = []
for i in list_1:
    if i not in list_2:
        list_3.append(i) 
print(list_3)