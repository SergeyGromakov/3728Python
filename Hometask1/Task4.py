# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

num_of_birds = int(input('Введите количество журавликов, которое Катя, Петя и Сергей сделали вместе: '))
if num_of_birds % 6 == 0:
    # привожу значения в int, чтобы отображались без десятичных знаков
    print (f'Петя и Сережа сделали по {int(num_of_birds / 6)}, а Катя {int(num_of_birds * 2 / 3)}')
else:
    print('У задачи при заданных условиях нет решения')