# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

first_class = int(input('Введите количество учеников первого класса: '))
second_class = int(input('Введите количество учеников второго класса: '))
fird_class = int(input('Введите количество учеников третьего класса: '))
print(
    f'Количество нужных парт {(first_class+1)//2 + (second_class+1)//2 + (fird_class+1)//2}')