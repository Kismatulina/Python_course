# Знакомство с языком Python (семинары)
# Урок 1. Ввод-Вывод, операторы ветвления
# Домашняя работа к семинару № 1 черновик

# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# print("Введите трехзначное число: ")
# n = int(input())
# summa = 0
# while n > 0 : # пока n > 0 выполняются действия:
#     x = n % 10  # в число х берем остаток от деления на 10 
#     summa = summa + x # в сумму добавляем это число 
#     n = n // 10 # делим наше число на целочисленное 10 
# print(summa) # выводим сумму 6 (1 + 2 + 3)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int (input())
# m = s/ 6 # сколько сделал Петр и Сергей каждый
# print(int(s/6)) # сделала Петр 
# print(int(m + m)* 2) # сделала Катя
# print(int(s/6)) # сделала Сергей


# s = int (input("Введите число жур"))
# print(int(s/ 6), int(s * 2/3), int(s/ 6))


# s = int(input( ))
# k = 6
# if s% k == 0: # если кратно 6 ( остаток от деления нет
#     print(f "Петя" {})
# else: 
#     print("не делится")



#s = int (input())
# m = '3'
# print(m ** 2)
# print(int(m) ** 2)

# s=-(n+m+k)//2 # не правильно говорти сложить все
# print(-s)
# iter *= 5

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# Решение: верное решение со Славой решала
# ticket = input()
# print((int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3])  + int(ticket[4]) + int(ticket[5])))

#ticket = ticket[:1] + ticket[1:2] + ticket[2:3]

#ticket = int(input(385916))
# ticket_sum = int(input(ticket[:1] + ticket[1:2] + ticket[2:3]))
#print(ticket)
# n = 5 - # узнать какой тип данных в переменной
#print(type(ticket))
# n = 'hdjkfl'
# print(type(n)) 

# ticket = ticket[-3] + ticket[-2] + ticket[-1]
# print(ticket)
#print(ticket[0] '+' [1] '+' [2])
#print(len(ticket))  
#print([:])  

# Решение:
# ticket = 385916
# print('Введите первое число: ') # три переменные сложила
# a = int(input())
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# print(a, ' + ', b, ' + ', c, ' = ', a + b + c) 



# Решение:
#print("Введите номер билета: ")
# n = int(input())
# count = 0
# summa1 = 0
# summa2 = 0
# #for i in range[0, 3]: # не знаю что поставить? Цикл for наша переменная i будет принимать значения от 0 до 2 индекса:
# for i in range[n]:
#     while n > 0 : # пока n > 0 выполняются действия:
#         x1 = n % 10  # в число х берем остаток от деления на 10 
#     summa1 = summa1 + x1 # в сумму добавляем это число 
#     n = n // 10 # делим наше число на целочисленное 10 
#     print(summa1) # выводим сумму первых 3 чисел

# for i in range(-3, -5): # Цикл for наша переменная i будет принимать значения от  до 2 индекса:
#     while n > 0 : # пока n > 0 выполняются действия:
#         x2 = n % 10  # в число х берем остаток от деления на 10 
#     summa2 = summa2 + x2 # в сумму добавляем это число 
#     n = n // 10 # делим наше число на целочисленное 10 
#     print(summa2) # выводим сумму 

# if summa1 == summa2:
#     print('yes счастливый билет')
# else:
#     print('no не счастливый билет')


# while count <= 3: # 
#     result += count #
# print(result)



# n = 385916 # сумма всех чисел
# summa = 0
# while n > 0 : # пока n > 0 выполняются действия:
#     x = n % 10  # в число х берем остаток от деления на 10 (6)
#     summa = summa + x # в сумму добавляем это число (0+6)
#     x = n % 10  # в число х берем остаток от деления на 100 (16 убираем)
#     summa = summa + x # в сумму добавляем это число () (3859)
#     x = n % 10  # в число х берем остаток от деления на 1000 (916)
#     summa = summa + x # в сумму добавляем это число () (385)
#     x = n % 10  # в число х берем остаток от деления на 10000 (5916)
#     summa = summa + x # в сумму добавляем это число (6+5916) (38)
#     n = n // 10 # делим наше число на целочисленное 10 (38:10=3 8)
# print(summa) # выводим сумму (0+6) +(6+1)+(7+9)+(16+5)+3+8=32








# n = int(input()) # вводит ползователь / не то
# f = 1          # факториал
# result = 1
# while f <= n: # лог.условие-пока f меньше или равно n,  это число от которого будем брать факториал 
#     result *= f #сама логика:в наш result запишем = result (1) * f ф(1) (result хранит текущее состояние факториал)
#     f += 1 # f=f+1 и к f единичку прибавляем и проверям меньше или равна она n, если меньше то result * f (и напечать первую цифру и снова)
# print(result)

# n = int(input()) # верное решение, не понятно
# f = 1
# result = 1
# while n != 0:
#     result += n # result = result * f
#     n += 1 # f=f+1
# print(result) # result = 1+5*4*3*2


# n = 423 # найти сумму всех чисел
# summa = 0
# while n > 0 : # пока n > 0 выполняются действия:
#     x = n % 10  # в число х берем остаток от деления на 10 (3)
#     summa = summa + x # в сумму добавляем это число (0+3)
#     n = n // 10 # делим наше число на целочисленное 10 (423:10=42)
# print(summa) # выводим сумму 4+2+3=9





# Управляющие конструкции: while-else пока - иначе
# a = int(input()) #пытаюсь
# i = 0 #  цикл
# while i < 5:
#     if i == 3:
#         print(a, '+', b, '+', c)   
#         break # получим 3, внутри else будет игнорироваться, так как цикл завершился не самостоятельно.
#     i = i + 1
# else:              # Пример программного кода без использования break: получим Пожалуй хватит 5
#     print('Пожалуй')
#     print('хватит )')
# print(i)



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Какое количество долек хотите отломить: " ))
# s= m * n 
# if s > k and  m % k == 0 or n % k == 0: # остаток от деления нет

#     print("делится")
# else: 
#     print("не делится")
s = m * n
if k > s:
    print('NO') # если количество долек больше суммы, нет
elif ((k % m == 0) or (k % n == 0)): # можно ли горизонтальными и вертик. разрезами получить необходимое количество долек
    print ('YES')
elif ((k % m != 0) or (k % n != 0)):
    print('NO')
else:
    print('NO')    


# n = 3
# m = 2
# k = int(input( ))
# print((k%n == 0) and (k//n <= m)) or ((k%m == 0) and (k//m <= n)) # Слава дал

#Задача с методом флажка (break лучше не использовать)
# Пользователь вводит число, необходимо найти минимальный делитель данного числа
# Решение:
# n = int(input())
# flag = True
# i = 2
# while flag: # наш цикл while будет выполняться пока наш флаг равен True
#     if n % i == 0: # если остаток при делении числа n на i равен 0,т.е мы нашли какойто делитель
#         flag = False # то меняем наш флаг на  False 
#         print(i) # и соответственно наш цикл завершает свою работу
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2 (не поняла делитель?)
#         print(n)
#         flag = False
#     i += 1