__version__ = "_1.0.1_"
'''
функция main и ее реализация

'''


from System_Interface import Menu_Bar
import os

# очищает поле  терминала
os.system('cls')


class Program:
    print("📓 Вас приветствует программа, телефонная книга.",
          "Версия программы ", __version__)

    def main():
        Menu_Bar()

    main()
