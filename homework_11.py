# Homework 11
# E. Plotnychenko
import json
import re

"""
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
"""


# 1
def file_reader(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        famous_math_list = json.load(json_file)
    return famous_math_list


# 2
def sort_surname(filename):
    famous_math_list = file_reader(filename)
    surname_list = [famous_math_dict["name"].split()[-1] for famous_math_dict in famous_math_list]
    return surname_list


# 3
def sort_by_dday(filename):
    famous_list = file_reader(filename)
    years_list = [int((re.findall(r'[0-9]+', famous_math_dict["years"])[1])) for famous_math_dict in famous_list]
    for index, math_dict in enumerate(famous_list):
        if "BC" in math_dict["years"]:
            years_list[index] = -1 * years_list[index]
    return years_list


def sort_by_dday_var_2(filename):
    famous_list = file_reader(filename)
    years_list = [int((re.findall(r'[0-9]+', famous_math_dict["years"])[1])) for famous_math_dict in famous_list]
    for index, math_dict in enumerate(famous_list):
        if "BC" in math_dict["years"]:
            years_list[index] = -1 * years_list[index]
    death_data_list = [abs(year) for year in sorted(years_list)]
    return death_data_list

# 4
def sort_len_text(filename):
    data_list = file_reader(filename)
    text_list = [text["text"].split() for text in data_list]
    return text_list


filename = "data.json"
name_sort = sorted(sort_surname(filename))
death_data_sort = sorted(sort_by_dday(filename))
death_data_sort_2 = sort_by_dday_var_2(filename)
text_len_sort = sorted(sort_len_text(filename), key=len)