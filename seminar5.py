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

# def fib(n):
#     if n in (0, 1):
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


# def fib(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     return fib(n - 2) + fib(n - 1)


# n = int(input('Vvedite chislo N: '))
# print(fib(n))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

# Равиль Арифулин
# import random

# def create_journal(n):
#     journal_=[]
#     for i in range(n):
#         journal_.append(random.randint(1,5))
#     return journal_

# def change_min_max(number_list):
#     min_number = min(number_list)
#     max_number = max(number_list)
#     for i in range(len(number_list)):
#         if number_list[i] == max_number:
#             number_list[i] = min_number
#     return number_list



# n = int(input('Введите количество оценок в классном журнале Василия: '))
# test_list = create_journal(n)
# print(test_list)
# test_list = change_min_max(test_list)
# print(test_list)

# Hashm Jahaf
# ocenki=[1,4,3,3,4]
# min_= min(ocenki)
# max_= max(ocenki)
# for i in range(len(ocenki)):
#     if ocenki[i] == max_:
#         ocenki[i]=min_
#     for i in ocenki]
# print(ocenki)


# Святослав Миловидов
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# Input: 5

# Output: yes

# def simple_num(num):
#     for i in range(2, num - 1):
#         if num%i == 0:
#             return 'No'
#     return 'Yes'
    
    
# print(simple_num(1))

# 37 задача
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3

# def reverse_input(n):
#     num = input('--> ')
#     if n == 1:
#         return num
#     return reverse_input(n - 1) + ' ' + num


# print(reverse_input(3))


# семинар 6
# задача 39
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
# Ввод: 					Вывод:
# 7					    3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1			(каждое число вводится с новой строки)

# # i = a.intersection(b) # i = {8, 2, 5} пересечение т.е найти те элементы, которые есть в обеих множествах
# n = int(input('Введите количество элементов: '))
# arr_1 = []
# for i in range(N):
#     a = int(input('Введите элемент массива: '))
#     arr_1.append(a)
    
# m = int(input('Введите количество элементов: '))
# arr_2 = []
# for j in range(M):
#     b = int(input('Введите элемент массива: '))
#     arr_2.append(b)

# new_arr = []
# def result(arr_1, arr_2):
#     for i in range(N):
#         if arr_1[i] not in arr_2:
#             new_arr.append(arr_2[i])
#     return(new_arr)

# print(result(arr_1, arr_2))

# друго
# def num_in(list_1: list[int | float], list_2: list[int | float]) -> list[int | float]:
#     print(number)
#     result = []
#     for num in list_1:
#         if num in list_2:
#             result.append(num)
#     return result


# list_1 = [3, 1, 3, 4, 2, 4, 12]
# list_2 = [4, 15, 43, 1, 15, 1]


# print(num_in(list_1, list_2))

# 1



# def func(a=None):
#     if a is None:
#         a = []
#     a.append(1)
#     print(a)

# func()
# func()
# func()



# 10:51
# def func(a=[]):
#     a.append(1)
#     print(a)

# func()
# func()
# func()

# зада 41
# Святослав Миловидов
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел. 

# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5		1 5 1 5 1

# Вывод:			Вывод:
# 0				2
				
# 				(каждое число вводится с новой строки)


arr_1 = list() # верное решение
counter = 0
n_1 = int(input('Введите кол-во эл-ов первого массива чисел: '))
for i in range(n_1):
    arr_1.append(int(input(f'Введите {i+1}й элемент массива: ')))

for i in range(1, (len(arr_1) - 1)):
    if arr_1[i - 1] < arr_1[i] > arr_1[i + 1]:
        counter += 1

print(counter)




# зада43
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3			2

# counter = 0

# for i in range(len(arr_1)):
#     for j in range(i + 1, len(arr_1)):
#         if arr_1[i] == arr_1[j]:
#             counter += 1

# print(counter)

# def result_(lst):  # 
#     counter = 0
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] == lst[j]:
#                 counter += 1
#     return(counter)

# вот поправил: def super_counter(arr_1):
#     counter = 0
#     for i in range(len(arr_1)):
#         for j in range(i + 1, len(arr_1)):
#             if arr_1[i] == arr_1[j]:
#                 counter += 1
#     return counter

# print(super_counter(arr_1))

# 1

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
#  каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284

# def sum_delitel(num):
#     result = 0
#     for delitel in range(1, num):
#         if num%delitel == 0:
#             result += delitel
#     return result
    
    

# k = 100000

# # number = 10
# # sum_number = 8
# # sum_for_sum_number = 7
# # number ?= sum_for_sum_number
# for number in range(2, k + 1):
#     sum_number = sum_delitel(number)
#     sum_for_sum_number = sum_delitel(sum_number)
#     if (sum_for_sum_number == number) and (number != sum_number) and (number < sum_number):
#         print(number, sum_number)