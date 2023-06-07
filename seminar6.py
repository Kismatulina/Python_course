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

# Ввод: 		Ввод:
# 5				5
# 1 2 3 4 5		1 5 1 5 1

# Вывод:		Вывод:
# 0				2
				
# 				(каждое число вводится с новой строки)


# arr_1 = list() # верное решение
# counter = 0
# n_1 = int(input('Введите кол-во эл-ов первого массива чисел: '))
# for i in range(n_1):
#     arr_1.append(int(input(f'Введите {i+1}й элемент массива: ')))

# for i in range(1, (len(arr_1) - 1)):
#     if arr_1[i - 1] < arr_1[i] > arr_1[i + 1]:
#         counter += 1

# print(counter)




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