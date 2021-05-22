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
def sort_surname(dict_list):
    surname_list = []
    surname_list.append(dict_list.get("name").split()[-1])
    return surname_list


# 3
def sort_by_dday(data_list):
    life_years = data_list.get("years")
    years_string = re.findall(r'[0-9]+', life_years)
    years_int = [int(year) for year in years_string]
    death_year = max(years_int) if "BC" not in years_int else -1 * min(life_years)
    return death_year


# # 4
def sort_len_text(data_list):
    info_text = data_list.get("text")
    return len(info_text)


filename = "data.json"
data_list = file_reader(filename)
name_sort = sorted(data_list, key=sort_surname)
death_data_sort = sorted(data_list, key=sort_by_dday)
text_len_sort = sorted(data_list, key=sort_len_text)