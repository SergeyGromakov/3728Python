# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
import random
N = int(input('Введите длину массива: '))
K = int(input('Введите значение для сдвига массива: '))
my_list = [random.randint(0, 10) for i in range(N)]
print(my_list)

# 1 вариант
print(my_list[-K:] + my_list[:-K])

# 2 вариант 
# for i in range(K):
#     element = my_list.pop()
#     my_list.insert(0, element)
#     i+=1
# print(my_list)