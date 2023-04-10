phone_book = []

file = open('sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
file.close()
for contact in data:
    new_contact = contact.strip().split(';')
    new_contact = {'name': new_contact[0],
                   'phone': new_contact[1],
                   'comment': new_contact[2]}
phone_book.append(new_contact)

phone_book.append({'name': 'Антон Пальчиков',
                   'phone': '999-999',
                   'comment': 'Друг Ноггано'})
print(phone_book)

new_phone_book = []
for contact in phone_book:
    new_contact = ';'.join([values for values in contact.values()])
new_phone_book.append(new_contact)

new_phone_book = '\n'.join(new_phone_book)

file = open('sample.txt', 'w', encoding='UTF-8')
file.write(new_phone_book)
file.close()

cont = '\nАнгелина Воробьева;4564654;Куртизанка'

file = open('sample.txt', 'a', encoding='UTF-8')
file.write(cont)
file.close()

with open('sample.txt', 'a', encoding='UTF-8') as file:
    file.write(cont)
