# 1. Открыть файл + 
# 2. Сохранить файл + 
# 3. Посмотреть все контакты +
# 4. Создать контакт +
# 5. Найти контакт +
# 6. Изменить контакт 
# 7. Удалить контакт
# 8. Выход

# def add_cont():
#     file = open('файл.txt', 'a', encoding='UTF-8')
#     data1 = input('введите ФИО: ')
#     data2 = input('номер телефона: ')
#     data3 = input('место работы: ')
#     data =  data1 + '; ' + data2 + '; ' + data3 + '\n'
#     print(data)
#     file.write(data)
#     file.close()

# def read_cont():
#     file = open('файл.txt', 'r', encoding='UTF-8')
#     data = file.readlines()
#     file.close()
#     for contact in data:
#         contact = contact.strip().split(';')
#         print(''.join(f'{e:<20}' for e in contact))


# def find_cont():
#     file = open('файл.txt', 'r', encoding='UTF-8')
#     data = file.readlines()
#     file.close()
#     search_cont = input('введите для поиска информацию: ')
#     num=0
#     for cont in data:
#         if search_cont.lower() in cont.lower():
#             cont = cont.strip().split(';')
#             print(''.join(f'{e:<20}' for e in cont))
#             num+=1
#     if num == 0:
#         print('Такого абонента нет в списке')

def change_cont():
    phone_book = []
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    i = 1
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact = {'id':i,
        'name':new_contact[0],
        'phone':new_contact[1],
        'comment':new_contact[2]}
        print(''.join(f'{e:<20}' for e in list(new_contact.values())))
        phone_book.append(new_contact)
        i+=1
    num_of_abonent = int(input('Введите порядковый номер абонента, который хотите изменить: '))
    num_of_change = int(input('Выберите, что вы хотите изменить: \n1. Имя, \n2. Номер телшефона, \n3. Место работы\n'))
    if num_of_change == 1:
        num_dict = phone_book[num_of_abonent-1]
        num_dict['name'] = input('Введите правильные Фамилию и Имя: ')
        phone_book[num_of_abonent-1] = num_dict

change_cont()