'''
Задача 14: Требуется вывести все 
целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.

'''

n = int(input(" Enter number N > "))
print(f" Your number {n} ")

result = int(1)
for i in range(1, int(n / 2)+1):
    print(result, end='\n')
    result = i + i
