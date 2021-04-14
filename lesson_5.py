# value = int(input("Введи целое число: "))
# try:
#     if value > 10:
#         print("Число больше 10")
#     else:
#         print("Число меньше или равно 10")
# except: # (здесь может быть любая ошибка)
#     pass # pass - выходит из проверки без вывода результата. Это обязательный параметр!!

# ord_value = ord("z") # функция ord выводит номер символа в таблице ASCII
# print(ord_value)
# chr_value = chr(98) # Функция chr выводит символ, который соответствует указаному номеру в таблице ASCII

# Сортировка. В Python есть уже встроенные сортировки
# my_list = [12, 34, 5, 1, -6, 100, -122]
# my_list.sort()# МЕТОД sort не сохраняет исходный список
# print(my_list)
# new_list = sorted(my_list)# ФУНКЦИЯ сохраняет исходный список при условии, что имя нового списка отличается от исходного
# new_list_1 = sorted(my_list, reverse=True)# Разворачивает сортировку (От большего к меньшему)
# print(max(my_list))# Самый большой объект списка
# print(min(my_list))# Самый маленький объект списка
# print(sum(my_list))# Сума элементов списка
# my_list = list("qwertyFGHAJS3124()!@#{=")
# new_list = sorted(my_list)# Сортирует по номеру символа в таблице ASCII
# print(new_list)


# РЕШЕНИЕ ЗАДАЧ
# Сколько раз встречается символ в строке
# my_str = "blablacar"
# my_symbol = "bla"
#
# result = my_str.count(my_symbol)# метод count считает количество раз, которые встречается символ

# Напечатать символ столько раз, сколько он встречается в строке

# my_str = "blablacar"
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# # symbol_list = [my_symbol] * count # КОСТЫЛЬ!!!!
# # for line in symbol_list:
# #     print(line)
# for _ in range(count): # метод range создает ДИАПАЗОН от 0 до того числа,сколько раз встречается символ;
#     # _ - no name переменная (просто переменная без имени)
#     print(my_symbol)

# Напечатать сколько РАЗНЫХ символов встречается в строке. Большие и маленькие буквы - один символ
# my_str = "bla BLA car!)-+"
# result_str = ""
# for symbol in my_str.upper():
#     if symbol not in result_str:
#         result_str += symbol
# print(len(result_str))

# Дана строка и пустой список. Заполнить список символами из строки, которые стоят на четных местах

# my_str = "asfghkajhgqjkhgqhjegk"
# my_list = []
# for symbol in my_str[::2]:
#     my_list.append(symbol)

# Дана строка и список целых чисел в диапазоне от 0 до длины строки минус 1. Заполнить второй список символами
# из строки, которые стоят на тех местах, которые указаны в списке с числами

# my_list = []
# my_str = "qwerty"
# str_index = [0, 1, 1, 4, 3, 2, 5, 0 , 1, 3, 5, 0, 0]
# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)