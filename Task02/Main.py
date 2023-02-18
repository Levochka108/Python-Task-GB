'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 

'''
print("This Program will find the sum of your three digits.")
user_number = int(input("Enter you number > "))
result = 0

while user_number > 0:
    result += user_number % 10
    user_number //= 10

print(f"Here is your sum > {result}")
