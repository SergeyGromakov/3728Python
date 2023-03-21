# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
num_of_coins = int(input('Введите количество монет: '))
count_null = 0
count_one = 0
for _ in range(num_of_coins):
    meaning = random.randint(0, 1)
    print(meaning)
    if meaning == 0:
        count_null += 1
    else:
        count_one += 1
    _ += 1
if count_one < count_null:
    print(f'Нужно перевернуть {count_one} монет')
else:
    print(f'Нужно перевернуть {count_null} монет')    


