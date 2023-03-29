import random
num = random.randint(0, 1001)
print(num)
num_low = 0
num_high = 1000
hidden = 500
while hidden != num:
    answ = input(f'Загаданное число больше {hidden}? : ')
    if  answ == '<' :
        num_high = (num_high+num_low)//2
    elif answ == '>' :
        num_low = (num_high+num_low)//2
    hidden = (num_high+num_low)//2
print(hidden)