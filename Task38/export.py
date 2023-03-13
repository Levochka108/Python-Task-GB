
"""
Функция открывает получает аргумент, в нашем случаи это наш фаил и выводт его на консоль.
"""

import time


def read_File(file):
    with open(file, 'r', encoding='utf-8') as data:
        print("Загрузка данных.")
        time.sleep(3)
        print("Подождите.")
        time.sleep(3)
        dictionary = data.read()

    return dictionary
