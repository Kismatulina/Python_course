# Знакомство с языком Python (семинары)
# Урок 7. Функции высшего порядка

# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-па

# a = str(input('Введите пара-ра-рам рам-пам-папам па-ра-па-дам   '))

# list_1 = list(пара-ра-рам рам-пам-папам па-ра-па-дам) # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз 
#     n = int(input()) # пользователь вводит целое число
#     list_1.append(n) # добавление (сохранение) элемента в конец! списка
# print(list_1)

# def same_by(func, vals):
#     return len(set(map(func, vals))) in [0, 1] # map(func, vals) выведит 0,0,0,0$ f set выведит уникальные не повторяющиеся значения множества
                          

# values = [0, 2, 10, 7]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: 
# print_operation_table(lambda x, y: x * y) 
# Вывод:
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 
num_rows = 6
num_columns = 6
# num_rows = 6
# num_columns = 6
# # operation_table 
# print_operation_table(lambda x, y: x * y) 

# operation_table = [] # создание пустого списка
# print(operation_table) # вывели пустой список []
# for i in range(6): # потом туда направились 0,1,2,3,4(i будет принимать значение от 0 до 4)
#     operation_table.append(i) # добавление в наш список значение i 
#     print(operation_table)
    # print_operation_table(lambda x, y: x * y) 
# # []
# # [0]
# # [0, 1]
# # [0, 1, 2]
# # [0, 1, 2, 3]
# # [0, 1, 2, 3, 4]

# Можно использовать вложенные циклы:
line = "" # создаем переменную line которая является в пустой строке
for i in range(1, num_rows + 1): # наша переменная range генерирует последовательность из пяти чисел,
 # значит наш цикл for будет выполняться 5 раз. (по сути выводим нашу строку из пяти звездочек)
    line = ""  #создаем пустую переменную line (для i получается - строки)
    for j in range(1, num_columns + 1): #еще раз проходимся т.е. 
    #     line += "i * j"  # к нашей строке 5 раз добавляем нашу звездочку (для столбцов)
    # print(line)  # печатать после цикла (нет отступа line += "*"-это находится в теле главного цикла for i и 
# # по сути выводим нашу строку из пяти звездочек)
       

# вятослав Миловидов
# Администратор
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table_list = []
#     for i in range(1, num_rows + 1):
#         line_list = []
#         for j in range(1, num_columns + 1):
#             el = operation(i, j)
#             line_list.append(el)
#         table_list.append(line_list)
    
#     for line in table_list:
#         print(*line)

# print_operation_table(lambda x, y: x*y)


# 2 
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             el = operation(i, j)
#             print(el, end=' ')
#         print()

# print_operation_table(lambda x, y: x*y)

# 3
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table_list = [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]
#     for line in table_list:
#         print(*line)

# print_operation_table(lambda x, y: x*y)