'''
функция main и ее реализация

'''
__version__ = "_1.0.0_"

from interface import choice
import os

# очищает поле  терминала
os.system('cls')


class Program:
    print("📓 Вас приветствует программа, телефонная книга.",
          "Версия программы ", __version__)

    def main():
        choice()

    main()
