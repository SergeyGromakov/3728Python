# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# num = int(input('Введите число, которое хотите проверить:'))
# count = 0
# for i in range(1, num+1):
#     if num%i == 0:
#         count += 1
# if count == 2:
#     print(f'Число {num} является простым')
# else:
#     print('Число не является простым')
    
def simple_num (num):
        for i in range(2, num):
            if num % i == 0:
                return 'Составное'
        return 'Простое'    
print(simple_num(9))            