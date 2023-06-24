# Знакомство с языком Python (семинары)
# Урок 8. Работа с файлами
# num = (1, 2)
# print(list(map(lambda x: x**2, num)))

# з 49
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# name1, fam1, surname1, phone1
# name2, fam2, surname2, phone2
# name3, fam3, surname3, phone3
# base = dict()
# n = r'seminar8\book.txt'

# with open('book.txt', 'r') as file:
#     def read_contacts(filename):
#         contacts =[]
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name': name,
#                 'surname': surname,
#                 'patronymic': patronymic,
#                 'phone': phone
#             }
#             contact.append(contact)
#         return contacts

# filename = r'book.txt'
# # filename = r'Python_course\seminar8.py\book.txt'# ЗДЕСЬ НЕ ПОЛУЧАЕТСЯ , НЕ ВИДИТ , В РУЧНУЮ ПРОБУЮ ПОСТАВИТЬ
# contact = read_contacts(filename)
# print(f'{contact}')


# СНОВА ЗАПИСЫВАЮ С РЕБЯТАМИ:
def write_contacts(filename):
    with open(filename, 'a', encoding='utf-8') as file: # чтобы читал кирилицу , не ругался на кирилицу
        file.write('\n' + input(f'Введите имя фамилию и отчество и номер телефона: '))
    return file # подумать как добавить контакт, сам список контактов не расширяется, здесь архитектура проект , надо менять не файл , а именно эту конструкцию 


def read_contacts(filename):
    contacts =[]
    with open(filename, 'r') as file:
        for line in file:
            name, surname, patronymic, phone = line.strip().split(',')
            contact = {
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'phone': phone
            }
            print(name, surname, patronymic, phone) # сказал здесь вывести Слава
            contacts.append(contact)
    return contacts
    
# скопировали снова и работаем здесь: хотели по фамилиям выводить
# def read_contacts(filename):
#     contacts =[]
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name': name,
#                 'surname': surname,
#                 'patronymic': patronymic,
#                 'phone': phone
#             }
#             contact.append(contact)
#         return contacts


filename = r'seminar8\book.txt' # 
a = int(input('1 - для ввода, 2 - для вывода \n'))
if a == 1:
    add_contact = write_contacts(filename)
elif a == 2:
    contact = read_contacts(filename) # здесь считали и надо подумать как его добавить
    # print(f'{contact}')  # сказал убрать Слава
else:
    print('Нет такой функции!')




# Святослав Миловидов
# Администратор для домашней на 9 или 8 показал
# def change_contact():
#     file_path = 'phone.txt'
#     contact_data = []
#     with open(file_path, 'r') as phone_book:
#         for line in phone_book:
#             contact_data.append(line.strip())
    
    
#     search_info = input('Какой контакт: ')
    
#     for contact_idx in range(len(contact_data)):
#         if contact_data[contact_idx] in contact:
#             new_info = input('Введите изменения: ')
#             contact_data[contact_idx] = new_info
#             break
    
#     with open(file_path, 'w') as phone_book:
#         for contact in contact_data[:-1]:
#             phone_book.write(contact + '\n')
#         phone_book.write(contact_data[-1])



