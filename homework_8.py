import random as rnd
import string


################################################
"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержатся
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
"""

def create_list(my_list):
    result_list = [value[::-1] if index % 2 else value for index, value in enumerate(my_list)]
    return result_list


################################################
"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержатся
элементы из my_list у которых первый символ - буква "a".
"""
def create_a_begin_list(my_list):
    my_result = [value for value in my_list if value[0] == "a"]
    return my_result


################################################
"""
3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержатся
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""
def create_a_list(my_list):
    my_result = [value for value in my_list if "a" in set(value)]
    return my_result


################################################
"""
4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
"""
def create_string_list(my_list):
    my_result = [value for value in my_list if type(value) == str]
    return my_result


################################################
"""
5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержатся те символы из my_str,
которые встречаются в строке только один раз.
"""

def create_symbols_list(some_string):
    my_result = [char_count for char_count in my_str if my_str.count(char_count) == 1]
    return  my_result


################################################
"""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""
def create_diff_symbols_list(my_str_1, my_str_2):
    my_result = list(set([symb for symb in my_str_1 if my_str_2.count(symb) > 0]))
    return my_result


################################################
"""
7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""
def create_one_symbols_list(my_str_1, my_str_2):
    my_result = [symb for symb in my_str_1 if my_str_1.count(symb) == 1 and my_str_2.count(symb) == 1]
    return my_result


################################################
"""
8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
"""
def generate_email(names, domains):
    rand_email = f"{rnd.choice(names)}.{rnd.randint(100, 999)}@{''.join(rnd.choice(string.ascii_lowercase) for _ in range(rnd.randrange(5, 7)))}{rnd.choice(domains)}"
    return rand_email



names = ["evil", "karlos", "michael", "otis", "kross", "polo"]
domains = [".net", ".com", ".ua", ".org"]
my_list = ["asd", "qwe", "fras", "are", "gjka", "acv", "pork", "all"]
my_list_1 = ["asd", 5, 4.32, "qwe", 112, "fras", (2, 4, "qwe"), 11.84, "bgaf"]
my_str = "qwtwbqhfsfavbzvnlzki lyiolusr!r"
my_str_1 ="aaabcdettgpo!ббю"
my_str_2 ="badddcfggtlk&"

result_1 = create_list(names)
result_2 = create_a_begin_list(my_list)
result_3 = create_a_list(my_list)
result_4 = create_string_list(my_list_1)
result_5 = create_symbols_list(my_list)
result_6 = create_diff_symbols_list(my_str_1, my_str_2)
result_7 = create_one_symbols_list(my_str_1, my_str_2)
result_8 = generate_email(names, domains)