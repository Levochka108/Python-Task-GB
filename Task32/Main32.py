
import random

# создаем список с рандомными числами
numbers = [random.randint(1, 100) for _ in range(20)]

# задаем значения мин и макс
min_value = int(input('Введите минимальное значение: >'))
max_value = int(input('Введите максимальное значение: >'))

indexes = []
for i in range(len(numbers)):
    if min_value <= numbers[i] <= max_value:
        indexes.append(i)

print(f'Список рандомных чисел > {numbers}')
print(
    f'Элементы списка с значениями от {min_value} до {max_value} имеют индексы: {indexes}')
