# Знакомство с языком Python (семинары)
# Урок 6. Повторение списков
# домашняя работа №6

# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input('Введите первый элемент '))
d = int(input('Введите разность этих чисел '))
n = int(input('Введите количество элементов '))
list1 = []
for i in range(n):
    an = a1 + i * d # (n-1)
    list1.append(an)
    print(list1)

# a1 = int(input(' '))
# d = int(input(' '))
# n = int(input(' '))
# for i in range(n):
#     print(a1 + i * d)




# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

#         0   1  2 3   4   5  6   7  8  9  10  11 12  13  14  15 16  17  18 19
arr_n = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
a = int(input('Введите минимальное значение диапазона   '))
b = int(input('Введите максимальное значение диапазона   '))

for i in range (len(arr_n)):
    if arr_n[i] > a and arr_n[i] < b:
        # return arr_n
        print(i)
else:
    print('Ввели не коректный диапазон') 