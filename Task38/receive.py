def get_input_info():
    info = []
    last_name = input('📝 Введите фамилию > ')
    info.append(last_name)
    first_name = input('📝 Введите имя > ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('📝 Введите номер телефона > ')
            if len(phone_number) != 11:
                print('❗️ В номере телефона должно быть 11 цифр. ❗️')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('❗️ Номер телефона должен состоять только из цифр. ❗️')
    info.append(phone_number)
    description = input('📝 Введите описание > ')
    info.append(description)
    print("📁 Запись завершина.")
    return info


def writе_scv_file(info):
    file = 'D:\GB\python\Task\DataBase_phone_book.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def write_txt_file(info):
    file = 'D:\GB\python\Task\data_book.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'👥Фамилия > {info[0]}\n\n👤Имя > {info[1]}\n\n📱Номер телефона > {info[2]}\n\n📝Описание > {info[3]}\n\n\n')
