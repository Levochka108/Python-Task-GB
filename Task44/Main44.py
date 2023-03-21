"""
импортируем pandas чтобы запустить
"""
import numpy as np
import pandas as pd
from test import testMainTask


lst = ['robot'] * 20
lst += ['human'] * 20


np.random.shuffle(lst)

# Созем словарь для кодирования категорий в числовые значения
cat_dict = {cat: i for i, cat in enumerate(set(lst))}

# Создаем пустой массив нужного размера и заполняем его нулями
one_hot = np.zeros((len(lst), len(cat_dict)))

# Заполняем массив единицами в соответствующих индексах
for i, cat in enumerate(lst):
    one_hot[i, cat_dict[cat]] = 1

# Создаем DataFrame с one hot столбцами
data = pd.DataFrame(one_hot, columns=cat_dict.keys())

print(data.head())
print()
# Тестируем get_dummies
print(testMainTask(lst))
print("this is finish test")
print("===================")
