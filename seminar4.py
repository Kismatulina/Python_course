# 4
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split(

#   input_str = 'a a a b c a a d c d d'.split()
# dict_count = {}

# # 'a': 3
# # 'b': 1
# # for let in input_str:
# #     if let in dict_count:
# #         print(f'{let}_{dict_count[let]}', end=' ')
# #         dict_count[let] += 1
# #     else:
# #         print(let, end=' ')
# #         dict_count[let] = 1

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
#  слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13  


# arr = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells""".lower().split(" ")
# print(len(set(arr)))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

for let in input_str:
    if let in dict_count:
        print(f'{let}_{dict_count[let]}', end=' ')
        dict_count[let] += 1
    else:
        print(let, end=' ')
        dict_count[let] = 1


n = int(input('Введите число: '))
count_w = int(input('Введите число: '))
count_w = int(input('Введите число: '))
while n != 0:


min_w = int(input('Введите вес первого арбуза: ')) # один арбуз мы запросили
max_w = min_w # первый арбуз мы считаем самым тяжелым
for i in range(count_w - 1):  # раз один арбуз мы уже запросили, тогда сколько запросить в range? (1, count_w(не включительно) или (count_w - 1).  )
    w = int(input('Введите вес арбуза: '))
    if w > max_w:  # если арбуз больше нашего мах, то это уже будет мах
        max_w = w
    elif w < min_w: # если арбуз меньше нашего min , то это уже будет min
        min_w = w    
print(min_w, max_w)


Zahar 11:53
chislo = 0
while True:
    num = int(input())
    if num > 0:
        if chislo < num:
            chislo = num
    else:
        break

print(chislo)


Ravil Arifulin 11:56 по карсивее
count_numbers = 1
number_ = int(input(f'Введите число {count_numbers}: '))   
maximum_ = number_                            
while number_ != 0:    
    count_numbers += 1                   
    number_ = int(input(f'Введите число {count_numbers}: ')) 
    if number_ > maximum_:
        maximum_ = number_
print(f'Наибольший элемент последовательности: {maximum_}')



Svyatoslav Milovidov 11:57
maxx = -1 моржовый оператор

while (num:=int(input('--> '))) != 0:
    if num > maxx:
        maxx = num

print(maxx)


def sum_delitel(num):
    result = 0
    for delitel in range(1, num):
        if num%delitel == 0:
            result += delitel
    return result
    
    

k = 100000

# number = 10
# sum_number = 8
# sum_for_sum_number = 7
# number ?= sum_for_sum_number
for number in range(2, k + 1):
    sum_number = sum_delitel(number)
    sum_for_sum_number = sum_delitel(sum_number)
    if (sum_for_sum_number == number) and (number != sum_number) and (number < sum_number):
        print(number, sum_number)