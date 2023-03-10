from os.path import exists
from file_writing import writе_scv_file, write_txt_file, get_input_info
from export import read_File


def view():
    print(read_File('DataBase_phone_book.txt'))


def record_info():
    info = get_input_info()
    writе_scv_file(info)
    write_txt_file(info)


def choice():
    flag = input(
        'Для продолжения работы нажмите \'1\', 0 для завершения работы... ')
    while (flag.lower() == '1'):
        path = 'DataBase_phone_book.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            '📲 Введите \'1\', если хотите записать новые данные, 0 если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == '1':
            record_info()
        else:
            print("Новый контакт.")
            view()
        flag = input(
            'Для продолжения работы нажмите \'1\', 0 для завершения работы... ')
    print('Программа завершена.')


def creating():
    file = 'D:\GB\python\Task\Task38\DataBase_phone_book.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

    print("Фаил создан.")
