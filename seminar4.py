# Знакомство с языком Python (семинары)
# Урок 4. Словари, множества и профилирование
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split(

# input_str = 'a a a b c a a d c d d'.split()
# dict_count = {}
# for let in input_str:
#     if let in dict_count:
#         print(f'{let}_{dict_count[let]}', end=' ')
#         dict_count[let] += 1
#     else:
#         print(let, end=' ')
#         dict_count[let] = 1

# # в основном зале:
# st = input('Введите символы: ')
# st = st.split()
# # print(st)
# count_dict={}
# for i in st:
#     if i in count_dict:
#         print(f'{i}_{count_dict[i]}')
#         count_dict[i]+=1
#     else:
#         print(i)
#         count_dict[i]=1


# задача № 27
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
#  слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13  


# arr = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells""".lower().split()
# print(len(set(arr)))  # перевели в нижний регистр  lower() и через split разделили, через set передали длину в множество и посчитали

# lst = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# dict = {}
# for let in lst:
#     dict[let.lower()] = 0
#     print(len(dict.keys())) # чтото вывел в столбик кучу цифр

# задача № 29
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах


# Zahar 11:53
# chislo = 0
# while True:
#     num = int(input())
#     if num > 0:
#         if chislo < num:
#             chislo = num
#     else:
#         break
# print(chislo)

# Zahar 11:53 без брейка:
# shich = True
# chislo = 0
# while True:
#     num = int(input())
#     if num > 0:
#         if chislo < num:
#             chislo = num
#     else:
#        shich = False
# print(chislo)


# Ravil Arifulin 11:56 по красивее
# count_numbers = 1
# number_ = int(input(f'Введите число {count_numbers}: '))   
# maximum_ = number_                            
# while number_ != 0:    
#     count_numbers += 1                   
#     number_ = int(input(f'Введите число {count_numbers}: ')) 
#     if number_ > maximum_:
#         maximum_ = number_
# print(f'Наибольший элемент последовательности: {maximum_}')



# через  while классическое решение:
# num = int(input('--> ')) # число запрашивает с новой строки, пока не будет нуль
# maxx = num
# while num != 0:
#     if num > maxx:
#         maxx = num
#     num = int(input('--> '))
# print(maxx)


# Svyatoslav Milovidov 11:57 моржовый оператор !!!значение можно задавать и в неудобных местах
# maxx = -1  #  за мах взяли сразу -1

# while (num:=int(input('--> '))) != 0: #(присвоить значение и тут же его запросить и тут сравнили с нулем)можем прям здесь запросить для num: двоеточие равно и сама запрашиваемая конструкция: int(input('--> ') и в скобки
#     if num > maxx: # если оно не равно нулю, проверяем
#         maxx = num  # и если что мах перезаписываем
# print(maxx)


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