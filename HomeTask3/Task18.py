# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
num_of_elements = int(input('Введите количество элементов массива: '))
my_list = [random.randint(0, 10) for i in range(num_of_elements)]
print(f'Получаем следующий массив: {my_list}')
search_element = int(input('Какое значение (или самое близкое) Вы хотите найти?: '))
difference = 1000
close_element = 0
for i in my_list:
    if i == search_element:
        print(f'Элемент {search_element} есть в массиве')
        break
    elif  abs(i-search_element) < difference:
        difference = i - search_element
        close_element = i
print(f'Самое близкое значение {close_element}')    
        

