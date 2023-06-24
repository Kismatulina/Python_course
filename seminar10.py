Знакомство с языком Python (семинары)
Урок 10. Построение графиков
как код питона обратить в *.exe
Святослав Миловидов
Администратор
Try/except: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
О том, как правильно оформлять путь к файлу (базовый вариант): https://pythonworld.ru/moduli/modul-os-path.html
Но лучше сразу так: https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru

Ребята, ниже интересные ссылки с разбором некоторых проектов. Берите интересующие и атакуйте)
Визуализация звуков (прикольно для плеера): https://vk.com/wall-79831840_59594
Как превратить код на Python в .exe: https://vk.com/@we_use_python-prevraschaem-kod-na-python-v-ispolnyaemyi-exe-fail
Превращение голоса в текст: https://vk.com/wall-174948538_4183
https://vk.com/@we_use_python-uchimsya-sozdavat-pakety-python
Работа с крутой библиотекой Selenium. Очень полезный инструмент, позволяет работать с баузером (парасить, автоматизировать действия и т.д.): https://vk.com/wall-79831840_58984
Крутая библиотека для работы с интерфейсами (PyQt): https://vk.com/wall-79831840_58959
Нейронка, которая знакомиться с девушками в Тиндере XD: https://vk.com/wall-194576836_13051


graph = sns.scatterplot(data=penguins.dropna(), x="species", y="island") #дропна убрать пропуски!!! Хью оттенок, сайс масса точки, вид показывает где живут , стайлс ,вместо острова поменять на вид пингвина
С наилучшими пожеланиями!
graph = sns.scatterplot(data=penguins.dropna(), x="bill_depth_mm", y="body_mass_g", hue = 'sex', size = 'body_mass_g', style = 'island')


from sqlalchemy import true
penguins = sns.load_dataset("penguins")
penguins.dropna(inplace = True) # делает копию даты без пропусков (NaN)
penguins.head()

https://pythonru.com/biblioteki/seaborn-plot




mport matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = penguins.iloc[:, 2]
y = penguins.iloc[:, 3]
z = penguins.iloc[:, 4]

ax.set_xlabel("Длина клюва")
ax.set_ylabel("Ширина клюва")
ax.set_zlabel("Длина ласты")

ax.scatter(x, y, z)



plt.show()
Добрый день!
# PairGrid
lst = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
g = sns.PairGrid(penguins[lst])
g.map(sns.scatterplot)
С наилучшими пожеланиями!

sns.heatmap(penguins.corr(), vmin=-1, vmax=1)