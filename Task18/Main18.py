"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

        *Пример:*

        5
        1 2 3 4 5
        6
        -> 5
"""

# Блок ввода
user_Enter = int(input("Enter > "))
user_list = []
temp_Max = 0
for i in range(1, user_Enter + 1, 1):
    user_list.append(i)
    if (temp_Max < i):
        temp = i


# Блок поиска
user_Find_Num = int(input("Find number > "))


# Блок вывода
print(user_Enter)
print(user_list)
print(user_Find_Num)
print(temp)
