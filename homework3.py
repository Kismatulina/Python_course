# Знакомство с языком Python (семинары)
# Урок 3. Списки и словари
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# def masgen(n):
 
#     for i in range(1,10):
#         mlist.append(i)
 
 
 
#     print(mlist)
#     print(mlist.count(n))
 
# if __name__ == '__main__':
 
#     mlist=[]
#     n=int(input())
#     masgen(n)

A = [int(i) for i in input().split()] #заполним список
X = int(input()) #пользователь вводит число, количество вхождений которого нужно подсчитать
print(A.count(X)) #выводим количество вхождений числа X в список A    




# Можно список заполнять не только при его создание, но и во время работы программы: по пересечению надо решить
# list_1 = list() # создание пустого списка пока закрою
# for i in range(5): # цикл выполнится 5 раз 
#     n = int(input()) # пользователь вводит целое число
#     list_1.append(n) # добавление (сохранение) элемента в конец! списка

# # for i in list_1: # for при нумерации,для того чтобы узнать какой элемент стоит на той или иной позиции.
#     print(list_1) # перебираем занчения в нашем списке и выводим в столбик # чтото не то получается 5 - >  [5]


# items = int(input())
# num = [0] * items
# for s in range (len(items))






# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


# a = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2} # решила , но без ввода 2 чисел. не понятно 
# b = {3, 6, 9, 12, 15, 18}
# i = a.intersection(b) #  пересечение т.е найти те элементы, которые есть в обеих множествах
# print(i) # {12, 6}



# count_numbers = 1
# number_ = int(input(f'Введите число {count_numbers}: '))   
# maximum_ = number_                            
# while number_ != 0:    
#     count_numbers += 1                   
#     number_ = int(input(f'Введите число {count_numbers}: ')) 
#     if number_ > maximum_:
#         maximum_ = number_
# print(f'Наибольший элемент последовательности: {maximum_}')


# домашка
# 20 задача
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# start_lst = [{"А": "1"}, {"В": "1"}, {"Е": "1"}, {"И": "1"}, {"Н": "1"}, {"О": "1"}, {"Р": "1"}, {"С": "1"}, {"Т": "1"}]
# print("Введите слово: ")
# a = input()
# print(start_lst["А"]) 
# print(start_lst)

# d = dict()  # создали пустой словарь и можем сами создавать свой ключ:
# d['А'] = '1' # чтобы добавлять какие то значения, мы должны в нашем словаре указать ключ q 
# d['В'] = '1' # чтобы добавлять какие то значения, мы должны в нашем словаре указать ключ q 
# print(d) # выведит в одну строку {'q': 'gwerty', 'w': 'werty'}


# print("Введите первое число: ") #- ввод данных через инпут, если числа, то инт добавить
# a = int(input())
# b = int(input("Введите второе число: "))
# print(a, '+', b, '=', a + b)

# for item in dictionary: # for (k,v) in dictionary.items(): как фор взаимодействует с нашим словарем?:
#     print(item)  # будут выводится только наши ключи: up left down right
#     print('{}: {}'.format(item, dictionary[item])) # если к словарю обращаться то сначала к ключу('{}: {}'.format(item,) и 2е к значению dictionary[item]

# Операции со множествами в Python
# a = {а, в, е, и, н, о, Р, С, Т}
# b = {а, в, е, и, н,}
# c = a.copy() # c = {1, 2, 3, 5, 8} можем скопировать из а
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение а и b и раз уникальные значения 2 будет один раз
# i = a.intersection(b) # i = {8, 2, 5} пересечение т.е найти те элементы, которые есть в обеих множествах

