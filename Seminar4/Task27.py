# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# list_origin = '''She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.'''
# list_origin = list_origin.lower()
# list_origin = list_origin.split()
# print(list_origin)
# set_origin = set(list_origin)
# print(set_origin)
# print(len(set_origin))
import string
my_text = ''' She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.'''
print(my_text)
punct = list(string.punctuation) + ['\n', '\t']

for i in punct:
    my_text = my_text.replace(i, ' ')
my_text = my_text.lower().split()
print(my_text)
print(len(set(my_text)))

dict_count = {}
for key in my_text:
    dict_count[key] = dict_count.get(key, 0) + 1
print(dict_count)    

