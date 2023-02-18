'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10

'''
print("Укажите количество журналов.")
x = int(input(" > "))
temp_number = int(x)

result_three_chaild = int(temp_number / 3)

temp_result_Kata = int(result_three_chaild * 2)

temp_result_Peta = int(result_three_chaild / 2)

temp_result_Sereja = int(result_three_chaild / 2)

print(x, "->", temp_result_Peta, temp_result_Kata,
      temp_result_Sereja, sep=' ')
