'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 

'''
print("This Program will find the sum of your three digits.")
user_number = int(input("Enter you number > "))
result = 0
temp_user_number = user_number

while user_number > 0:
    result += user_number % 10
    user_number //= 10

print(f"Here is your sum > {result}")

# Единицы
result00 = temp_user_number % 10
print(f"1 > {result00}")
# Десятки
result01 = temp_user_number % 100
print(f"2 > {result01//10}")
# Сотни
result02 = temp_user_number % 1000
print(f"3 > {result02//100}")

print(f"Sum -> {result00+(result01//10)+(result02//100)} ({result02//100} + {result01//10} + {result00})", end=' Вот так вот!')
