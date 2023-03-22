# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 
import random
num_of_elem = int(input('Введите количество элементов: '))
my_list = [random.randint(0, 9) for i in range(num_of_elem)]
print(my_list)
count = 0
# for i in range(len(my_list)-1):
#     if my_list[i] < my_list[i+1]:
for i in range(1, len(my_list)):
    if my_list[i-1] < my_list[i]:
        count +=1
print(count)