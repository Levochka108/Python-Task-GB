'''
Функция открывает на чтение фаил.
'''
import time


def read_File(file):
    try:
        with open(file, 'r', encoding='utf-8') as data:
            print("Загрузка данных.")
            time.sleep(3)
            print("Чтение данных.")
            dictionary = data.read()
            time.sleep(3)
            print("Чтение зарыто.")
        return dictionary
    except FileNotFoundError:
        content = "<<< NOT FOUND >>>"
    print(content)
