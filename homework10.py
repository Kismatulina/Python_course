# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() #|


# Статья про one hot вид
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет".
# "Зачет" ставится, если Слушатель успешно выполнил задание.
# "Незачет" ставится, если Слушатель не выполнил задание.

# Критерии оценивания:
# 1 - Слушатель написал корректный код для задачи, результат работы правильный за счет, которого можно перевести его в one hot вид и все корректно работает без ошибок.


# это выслала Анчен ссылку:
# import pandas as pd 
# import numpy as np 
# import random
 
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# print(data)
# #==================================================#
# data['tmp'] = 1
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value = 0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None
# print(data)


# Один из способов преобразовать этот DataFrame в one hot вид - использовать метод pandas get_dummies():

one_hot = pd.get_dummies(data['whoAmI'])

# Однако, если нужно реализовать это без использования данного метода, можно воспользоваться методом Pandas concat():

# Создаем пустой DataFrame one_hot, который будем наполнять
one_hot = pd.DataFrame()

# Для каждого уникального значения в столбце whoAmI создаем отдельный столбец в one_hot
for value in data['whoAmI'].unique():
    one_hot[value] = (data['whoAmI'] == value).astype(int)

# Результат выполнения кода:

# Изначальный DataFrame
#     whoAmI
# 0   human
# 1   human
# 2   robot
# 3   human
# 4   robot
# 5   robot
# 6   human
# 7   robot
# 8   robot
# 9   human
# 10  robot
# 11  human
# 12  robot
# 13  human
# 14  human
# 15  human
# 16  robot
# 17  robot
# 18  robot
# 19  human

# # Результат one hot
#     human   robot
# 0   1       0
# 1   1       0
# 2   0       1
# 3   1       0
# 4   0       1
# 5   0       1
# 6   1       0
# 7   0       1
# 8   0       1
# 9   1       0
# 10  0       1
# 11  1       0
# 12  0       1
# 13  1       0
# 14  1       0
# 15  1       0
# 16  0       1
# 17  0       1
# 18  0       1
# 19  1       0

# Davyd.AR, [21.06.2023 15:52]
# Есть второй вариант, но по нему сомнения. Вместо функции - метод

# Davyd.AR, [21.06.2023 15:53]
# Комменты не тёр, это решение предложила нейронка:

# Да, можно выполнить One-Hot Encoding без использования функции get_dummies, используя метод pandas Series.str.get_dummies() и объединение DataFrame используя метод pandas DataFrame.join(). Вот код:

import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Series str.get_dummies() method
one_hot = data['whoAmI'].str.get_dummies()

# Join the one-hot encoded data back to the original dataframe
data = data.join(one_hot)

print(data.head())


# В результате выполнения этого кода мы получим DataFrame, который будет содержать столбец 'whoAmI' и два бинарных столбца 'human' и 'robot',
#  таким образом каждая строка будет соответствовать только одному классу:


#     whoAmI  human  robot
# 0   robot    0      1
# 1   robot    0      1
# 2   human    1      0
# 3   human    1      0
# 4   human    1      0