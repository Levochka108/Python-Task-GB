"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; 
                                                         D, G – 2 очка; 
                                                         B, C, M, P – 3 очка; 
                                                         F, H, V, W, Y – 4 очка; 
                                                         K – 5 очков; 
                                                         J, X – 8 очков; 
                                                         Q, Z – 10 очков. 
                        А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
                                                         Д, К, Л, М, П, У – 2 очка; 
                                                         Б, Г, Ё, Ь, Я – 3 очка; 
                                                         Й, Ы – 4 очка; 
                                                         Ж, З, Х, Ц, Ч – 5 очков; 
                                                         Ш, Э, Ю – 8 очков; 
                                                         Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

        *Пример:*

        ноутбук
        12

        
        grasshopper
        19
"""

# Выбор языка
user_Lenguange = input("Enter Lenguage ru/en >>> ")
if (user_Lenguange == "en"):
    # Блок ввода
    string_Temp = input("Enter sting > ")

    temp_Data_Eng = {1: str("AEIOULNSTR"),
                     2: str("DG"),
                     3: str("BCMP"),
                     4: str("FHVWY"),
                     5: str("K"),
                     6: str("JX"),
                     7: str("QX"),
                     0: str(" ")}

    # Блок обработки
    result = 0
    for i in string_Temp:
        for j in temp_Data_Eng:
            if i.upper() in temp_Data_Eng[j]:
                result += j
    # Блок вывод
    print(result)

if (user_Lenguange == "ru"):
    string_Temp = input("Ввод текста > ")

    temp_Data_Rus = {1: str("АВЕИНОРСТ"),
                     2: str("ДКЛМПУ"),
                     3: str("БГЁЬЯ"),
                     4: str("ЙЫ"),
                     5: str("ЖЗХЦЧ"),
                     6: str("ШЭЮ"),
                     7: str("ФЩЪ"),
                     0: str(" ")}
    result = 0
    for i in string_Temp:
        for j in temp_Data_Rus:
            if i.upper() in temp_Data_Rus[j]:
                result += j
    # Блок вывод
    print(result)
