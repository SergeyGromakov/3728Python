# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# поскольку в питоне я не знаю строчные массивы, то преджполагаю, что номер будет int, т.е. не может начинаться с 0
number = int(input('Введите шестизначный номер транспортного билета: '))
if number < 100000 or number > 999999:
    print('Вы ввели не шестизначное число')
else:
    num1 = number // 1000
    num2 = number % 1000
    sum1 = num1%10 + num1//10%10 + num1//100
    sum2 = num2%10 + num2//10%10 + num2//100
    if sum1==sum2:
        print('Билет счастливый')
    else:
        print('Билет обычный')    