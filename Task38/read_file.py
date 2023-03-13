'''
Функция открывает на чтение фаил.
'''


def from_file(file):
    with open(file, 'r', encoding='utf-16') as data:
        dictionary = data.read()
    return dictionary
