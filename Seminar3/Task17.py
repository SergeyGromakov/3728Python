# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
import random
my_list = [random.randint(0, 10) for i in range(10)]
print(my_list)
print(set(my_list))
print(len(set(my_list)))