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

vinny_words = input("Введите стихотворение: ") # 
lett_count = lambda sentensis: sum([1 for letter in sentensis if letter.lower() in "аеёиоуыэюя"]) # определяем ф для подсчета гласных в предложении(sentensis) и letter.lower в нижний регистр ввели
phrases = vinny_words.split() # сплит разделил по пробелам фразы 
# print(vinny_words)
vowels_in_phrases = [lett_count(phrase.replace("-", "")) for phrase in phrases] # идем по строке гласные буквы в фразе, подсчтитанных гласные lett_count заменяем тире на пусто и заводим новую функцию phrase  
print('Парам пам-пам'if vowels_in_phrases.count(vowels_in_phrases[0]) == len(vowels_in_phrases) else 'Пам парам') # цикл сразу сравниваю значение гласных,
# если кол-во гласных букв в фразе (хранятся индексы) равны длине гласных букв, выводим Парам пам-пам иначе Пам парам  

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

# 1 вариант
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


# 2 вариант
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             el = operation(i, j)
#             print(el, end=' ')
#         print()

# print_operation_table(lambda x, y: x*y)

# 3 вариант
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table_list = [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]
#     for line in table_list:
#         print(*line)

# print_operation_table(lambda x, y: x*y)