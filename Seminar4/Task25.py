# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

import string
import random
all_chars = string.ascii_lowercase + string.digits
my_string = [random.choice(all_chars) for _ in range(30)]
print(my_string)
dict_count = {}

for i in my_string:
    dict_count[i] = dict_count.get(i, -1) + 1
    if dict_count.get(i) >0:
        print(f'{i}_{dict_count.get(i)}', end = ' ')
    else:
        print(i, end = ' ')    

# my_string = input('Введите строку для анализа: ')
# my_string = list(my_string)
# for i in range(-1, -(len(my_string)), -1):
#     count = 0
#     for j in range(len(my_string)+i):
#         if my_string[j] == my_string[i] and my_string[i] != ' ':
#             count += 1
#     if count != 0:
#          my_string[i] = my_string[i] + '_' + str(count)
# print(" ".join(my_string))            
