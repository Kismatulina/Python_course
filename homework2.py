# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)
# Домашняя работа к семинару № 2
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# 
total = int(input('Введи количество монет: '))
import random
items = [random.randint(0, 1) for i in range(total)]
print(*items, sep = '   ') 
print(sum(items) if sum(items) < total/2 else total - sum(items))


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import random 
s = int(input("Введите первое число: "))
p = int(input("Введите второе число: "))
x = random.randint(1, s)
y = s - x # s = y + x
while x * y != p: # если их перемножить и они не равны произведению, надо сгенерировать новый Х, но который не превосходит сумму s
    x = random.randint(1, s) # надо сгенерировать новый Х, но который не превосходит сумму s
    y = s - x # и  y присвоить снова s - x
print(x,y)




# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2 в степени k), не превосходящие числа N. 10 -> 1 2 4 8

n = int(input('Введи число N: '))
arr =[]
result = 1
while result <= n: # пока меньше n , делай:
    arr.append(result) #  append -сохранение элемента в конец списка
    result *=2 # переменную result умножай на 2 -> # result = 1 * 2
    print(*arr)

