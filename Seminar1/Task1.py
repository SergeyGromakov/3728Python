# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.


per_day = int(input('Сколько машина проезжает за день: '))
total_distance = int(input('Сколько машина проезжает всего: '))

print(f'Машине потребуется {(total_distance+per_day-1)//per_day} дней')