# 1. Посмотреть все контакты +
# 2. Создать контакт +
# 3. Найти контакт +
# 4. Изменить контакт + 
# 5. Удалить контакт 
# 6. Выход

def add_cont():
    file = open('файл.txt', 'a', encoding='UTF-8')
    data1 = input('введите ФИО: ')
    data2 = input('номер телефона: ')
    data3 = input('место работы: ')
    data = '\n' + data1 + ';' + data2 + ';' + data3
    print(data)
    file.write(data)
    file.close()
    start_function()

def read_cont():
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        contact = contact.strip().split(';')
        print(''.join(f'{e:<20}' for e in contact))
    start_function()

def find_cont():
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('введите для поиска информацию: ')
    num=0
    for cont in data:
        if search_cont.lower() in cont.lower():
            cont = cont.strip().split(';')
            print(''.join(f'{e:<20}' for e in cont))
            num+=1
    if num == 0:
        print('Такого абонента нет в списке')
    start_function()

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
    elif num_of_change == 2:
        num_dict = phone_book[num_of_abonent-1]
        num_dict['phone'] = input('Введите новый номер телефона: ')
        phone_book[num_of_abonent-1] = num_dict
    elif num_of_change == 3:
        num_dict = phone_book[num_of_abonent-1]
        num_dict['comment'] = input('Введите новое место работы: ')
        phone_book[num_of_abonent-1] = num_dict
    new_phone_book = []
    for contact in phone_book:
        del contact['id']

    new_contact_book = []
    for contact in phone_book:
        new_contact = ';'.join(f'{e}' for e in contact.values())
        new_contact_book.append(new_contact)
    new_contact_book = '\n'.join(new_contact_book)

    file = open('файл.txt', 'w', encoding='UTF-8')
    file.write(new_contact_book)
    file.close()
    start_function() 

def delete_contact():
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
    num_of_abonent = int(input('Введите порядковый номер абонента, который нужно удалить: '))
    phone_book.pop(num_of_abonent-1)
    print('Оставшиеся контакты: ')
    for contact in phone_book:
        del contact['id']
        print(''.join(f'{e:<30}' for e in list(contact.values())))
    
    new_contact_book = []
    for contact in phone_book:
        new_contact = ';'.join(f'{e}' for e in contact.values())
        new_contact_book.append(new_contact)
    new_contact_book = '\n'.join(new_contact_book)

    file = open('файл.txt', 'w', encoding='UTF-8')
    file.write(new_contact_book)
    file.close()
    start_function()

def start_function():
    num_of_choice = int(input('''\nВыберите, что вы хотите сделать со справочником: 
    1. Просмотреть все контакты
    2. Создать контакт 
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выйти из программы \n'''))
    if num_of_choice == 1:
        read_cont()
    elif num_of_choice == 2:
        add_cont()
    elif num_of_choice == 3:
        find_cont()  
    elif num_of_choice == 4:
        change_cont()
    elif num_of_choice == 5:
        delete_contact()
    elif num_of_choice == 6:
        print('Спасибо, до новых встреч!')

start_function()   
           

