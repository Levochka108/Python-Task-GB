'''
Задача 14: Требуется вывести все
целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.

 10 > 1, 2, 4, 8
 20 > 1, 2, 4, 8, 16
 100 > 1, 2, 4, 8, 16, 32, 64
'''

n = int(input(" Enter number N > "))
print(f" Your number {n} ")

# Написал методом тыка, плохо понял что нужно десть чтобы код работал как надо
result = int(1)
for i in range(1, n):
    if (2 ** i < n * 2):
        print(result, end='\n')
        result = 2 ** i

'''
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
'''