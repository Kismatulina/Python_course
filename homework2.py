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

# m = int(input('Введите колисество монет: ')) # 
# count_days = 0
# max_temp = 0
# for num_day in range(1, m + 1): # пе редали в range дни 1,2,3 и тд.(Запрашиваем эти наши дни)(for num_day inrange(days) будет показывать 0,1,2 это убрали)
#     day = int(input(f'Введите темп. в день {num_day}: ')) # нам надо в конкретный день запросить температуру
#     if day > 0: # если текущий день не отрицательный, то надо увеличить счетчик (нашли оттепели)
#         count_days += 1
#     else:
#         if count_days > max_temp: # из этих дней оттепелей найдем мах, проверяем больше предыдущей?,то записываем мах
#             max_temp = count_days
#         count_days = 0 # а счетчик обнуляем, т.к оттепель завершилась
# print(max_temp) # и выводим дни с мах температурами

#Задача 12:
# count_w = int(input('Введите колисество монет: '))
# min_w = int(input('Введите вес первого арбуза: ')) # один арбуз мы запросили
# max_w = min_w # первый арбуз мы считаем самым тяжелым

# for i in range(count_w - 1):  # раз один арбуз мы уже запросили, тогда сколько запросить в range? (1, count_w(не включительно) или (count_w - 1).  )
#     w = int(input('Введите вес арбуза: '))
#     if w > max_w:  # если арбуз больше нашего мах, то это уже будет мах
#         max_w = w
#     elif w < min_w: # если арбуз меньше нашего min , то это уже будет min
#         min_w = w    
# print(min_w, max_w)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2 в степени k), не превосходящие числа N. 10 -> 1 2 4 8

# n = int(input()) # другое решение без факториала: нужно основание 2 !
# result = 1                                          # result = 1 
# while n != 1:   # пока n не равен единице, делай:
#     result *= n # переменную result умножай на 5 -> # result = 1 * 5
#     n -= 1      # от n отняли единицу и возврат в цикл 4!=1 -> умножай 5*4 -> 4-1=3 и т.д
# print(result)   # result = 1*5*4*3*2

# iter = 2
# iter = iter**10 
# print(iter)   # получили два в степени 10 

# n = int(input())
# flag = True
# i = 2
# while flag: # наш цикл while будет выполняться пока наш флаг равен True
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False # то меняем наш флаг на  False 
#         print(i) # и соответственно наш цикл завершает свою работу
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2 (не поняла делитель?)
#         print(n)
#         flag = False
#     i += 1

list_1 = []
for i in range(1, 11): 
    list_1.append(i) #  append -сохранение элемента в конец списка
    list_1 = [i for i in range(1, 101)] #  append -сохранение элемента в конец списка
print(list_1) # [1, 2, 3,..., 10] Создать список чисел от 1 до 10

# Знакомство с языком Python (семинары)
# Урок 3. Списки и словари
# Домашняя работа к семинару № 3
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X 
# 5
# 1 2 3 4 5
# 3
# -> 1

# list_1 = []
# for i in range
# x = int(input('Введите сколько учеников в первом классе: '))
# print("Введите трехзначное число: ")
# n = int(input())