# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
Первый вариант:
import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, one_hot_data], axis=1)
data.head()

Второй вариант:
import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categ = data['whoAmI'].unique()
one_hot_data = pd.DataFrame(0, index=np.arange(len(data)), columns=categ)
for i in range(len(data)):
  categ = data.loc[i, 'whoAmI']
  one_hot_data.loc[i, categ] = 1
  data = pd.concat([data, one_hot_data], axis=1)

  data.head()
