'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
'''

n = int(input("Число N > "))
count = 1
while True:
    if (count == n):
        break
    count += count
    print(count)