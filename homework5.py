# Знакомство с языком Python (семинары)
# Урок 5. Рекурсия и алгоритмы
# домашняя работа №5
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число   '))
b = int(input('Введите число   '))
def stepen(a, b):
    if b == 0:  # базис любое число внулевой степени = 1
        return 1
    else:
        return(a**b) # рекурсия
print(stepen(a, b)) # печатаем то что в функции def


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
a = int(input('Введите число   '))
b = int(input('Введите число   '))
def sum(a, b):
    if b == 0: # базис
       return a
    return sum(a+1, b-1) # рекурсия
print(sum(a, b))



