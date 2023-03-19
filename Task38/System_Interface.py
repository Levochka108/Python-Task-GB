from os.path import exists
from receive import writе_scv_file, write_txt_file, get_input_info
from get_read import read_File as rf
import os
import time


def view():
    print(rf('DataBase_phone_book.txt'))


def record_info():
    info = get_input_info()
    writе_scv_file(info)
    write_txt_file(info)


def Menu_Bar():
    flag = input(
        'Для продолжения работы нажмите \'1\', 0 для завершения работы... ')
    print("Укажите путь сохранения данных")
    path = input(" > ")
    folder_name = "save"
    full_path = os.path.join(path, folder_name)

    while (flag.lower() == '1'):
        path = 'DataBase_phone_book.csv'
        valid = exists(path)
        if not valid:
            creating(path)
        choice_action = input(
            '📲 Введите \'1\', если хотите записать новые данные, 0 если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == '1':
            record_info(path)
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'1\', 0 для завершения работы... ')
    print('Программа завершена.')


def creating(x):

    # full_path = os.path.join(path, folder_name)

    # указываем путь и название папки
    # print("Укажите путь сохранения данных")
    # path = input(" > ")
    # folder_name = "save"

    # комбинируем путь и название папки
    # full_path = os.path.join(path, folder_name)

    # создаем пустую папку
    try:
        os.mkdir(x)
        print(f"Папка {x} успешно создана.")
    except FileExistsError:
        print(f"Папка {x} уже существует.")

    file_csv = f'{x}\DataBase_phone_book.csv'
    time.sleep(3)
    with open(file_csv, 'w') as data:
        print("Фаил создан csv.")
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

    file_txt = f'{x}\DataBase_phone_book.txt'
    with open(file_txt, 'w') as data:
        print("Фаил создан txt.")
        data.write(
            f'Телефонная книга\n')
