"""
Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 

Также нельзя использовать циклы.

"""



from BitWise import SUMMA

a, b = int(input(" A > ")), int(input(" B > "))

print(SUMMA(a, b))