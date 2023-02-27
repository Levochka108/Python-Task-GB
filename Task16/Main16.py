"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число 
X в массиве A[1..N]. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

"""
# Заполнение массива, массив размером до веденного пользователем числа.
user_list = []
user_EntNum = int(input("Enter number > "))

for i in range(0, user_EntNum + 1):
    user_list.append(i)

  # Блок поиска
user_FindNum = int(input("What number to look for? > "))
result_Find = 0
for i in user_list:
    if (user_FindNum == i):
        result_Find += 1

  # Блок вывода
print(user_EntNum)
print(*user_list[1: user_EntNum])
print(user_FindNum)
print(result_Find)


# Блок теста
user_EntNum_test = int(input("First test Enter > "))
user_list_test = []

user_FindNum_test = int(input("What number to look for? > "))
result_Find_test = 0
for k in range(1, user_EntNum_test + 1):
    user_list_test.append(int(input("Test Enter > ")))
    print(f'Complite > {k}')

for k in user_list_test:
    if (user_FindNum_test == k):
        result_Find_test += 1

    # Блок вывода теста
print(user_EntNum_test)
print(*user_list_test)
print(user_FindNum_test)
print(result_Find_test)
