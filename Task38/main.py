__version__ = "_1.0.0_"
'''
функция main и ее реализация

'''


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
