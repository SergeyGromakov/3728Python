# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

  
first_elem = int(input('Введите значение 1го элемента:'))
dif = int(input('Введите значение разницы: '))
num = int(input('Введите количество элементов прогрессии: '))
for i in range(num):
        elem = first_elem + dif * i
        print(elem, end = ' ')
