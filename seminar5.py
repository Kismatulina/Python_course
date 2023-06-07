# Знакомство с языком Python (семинары)
# Урок 5. Рекурсия и алгоритмы

# # семинра 5
# # Задача №31. Общее обсуждение
# # Последовательностью Фибоначчи называется
# # последовательность чисел a0
# # , a1
# # , ..., an
# # , ..., где
# # a0
# #  = 0, a1
# #  = 1, ak
# #  = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи
# # Input: 7
# # Output: 21

# def fib(n):    #  базовый , не знаешь что делать, разделяй и влавствуй, здесь просто если 1й и 2й это единица, верни 1
#     if n in (0, 1): # почему  нулевой и первый? 0 1 1 2фиб
#         return 1
#     return fib(n-1) + fib (n-2)


# m = int(input('Введите n: '))
# print(fib(m))

# Святослав Миловидов
# def fib(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)


# def fib(n):     # это рекурсия
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1  # без else, то же самое говорит
#     return fib(n - 2) + fib(n - 1)

# n = int(input('Vvedite chislo N: '))
# print(fib(n))


# задача № 35
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Равиль Арифулин
# import random
# def create_journal(n):
#     journal_=[]
#     for i in range(n):
#         journal_.append(random.randint(1,5))
#     return journal_

# def change_min_max(number_list):  # сначала функция, потом код внизу
#     min_number = min(number_list)
#     max_number = max(number_list)
#     for i in range(len(number_list)):
#         if number_list[i] == max_number:
#             number_list[i] = min_number
#     return number_list

# # это код^ кажется что уже завершили на функции вверху ^
# n = int(input('Введите количество оценок в классном журнале Василия: '))
# test_list = create_journal(n)
# print(test_list)
# test_list = change_min_max(test_list)
# print(test_list)

# Hashm Jahaf простое по индексам - макс присвоить мин  !!!!!
# ocenki=[1,4,3,3,4]
# min_= min(ocenki)
# max_= max(ocenki)
# for i in range(len(ocenki)):
#     if ocenki[i] == max_:
#         ocenki[i] = min_
# print(ocenki)

# ocenki=[1, 4, 3, 3, 4]
# min_ = min(ocenki)
# max_ = max(ocenki)
# ocenki2 = [min if i == max else i for i in ocenki] # если ай мах, сделай мин-пока не трогаем это
# print(ocenki2)

# Святослав Миловидов
# задача № 35
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

# def simple_num(num):
#     for i in range(2, num - 1): # если делится на 1, и само число на себя делится, то диапазон от двойки до самого num (себя)т.е в промежутке берем от 1 до числа
#         if num%i == 0:
#             return 'No' # не простое число
#     return 'Yes' # простое число
  
# print(simple_num(8)) # здесь числа сюда подставляют 8 - нет, верно не простое, делится на 1,2,8

# 37 задача
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3



# базовый случай: рекурсивный всегда приближает к базовому
# def reverse_input(n):
#     if n == 1:
#         num = input()  
#     return num

# рекурсивный метод:    
# def reverse_input(n):
#     num = input('--> ')
#     if n == 1:
#         return num
#     return reverse_input(n - 1) + ' ' + num

# print(reverse_input(3))


