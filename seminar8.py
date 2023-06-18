
num = (1, 2)
print(list(map(lambda x: x**2, num)))

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


Святослав Миловидов
Администратор для домашней
def change_contact():
    file_path = 'phone.txt'
    contact_data = []
    with open(file_path, 'r') as phone_book:
        for line in phone_book:
            contact_data.append(line.strip())
    
    
    search_info = input('Какой контакт: ')
    
    for contact_idx in range(len(contact_data)):
        if contact_data[contact_idx] in contact:
            new_info = input('Введите изменения: ')
            contact_data[contact_idx] = new_info
            break
    
    with open(file_path, 'w') as phone_book:
        for contact in contact_data[:-1]:
            phone_book.write(contact + '\n')
        phone_book.write(contact_data[-1])

        