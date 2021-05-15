# Homework 9
# E. Plotnychenko
import re
################################################
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""
# def create_domains_list(filename):
#     with open(filename, "r") as txt_files:
#         domains_list = txt_files.readlines()
#     new_domains_list = [value.lstrip(".") for value in domains_list]
#     return new_domains_list

################################################
"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""
# def create_surnames_list(filename):
#     with open(filename, "r") as txt_files:
#         object_list = txt_files.readlines()
#     strings_split_list = [my_str.split("\t") for my_str in object_list]
#     surnames_list = [surname[1] for surname in strings_split_list]
#     return surnames_list

################################################
"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""

def create_list(filename):
    data_list = []
    with open(filename, "r") as txt_files:
        info_list = txt_files.readlines()
    info_list = [value.split("-") for value in info_list]
    for info in info_list:
        for value in info:
            if len(info) > 1:
                data_list.append(value.split())
    return data_list
month_dict = {"January": "01",
              "February": "02",
              "March": "03",
              "April": "04",
              "May": "05",
              "June": "06",
              "July": "07",
              "August": "08",
              "September": "09",
              "October": "10",
              "November": "11",
              "December": "12"
              }

filename = "authors.txt"
info_list = create_list(filename)
print(info_list)



#
# # Вероятно, изобретаю велосипед
# def date_transform(filename):
#     date_list = strip_strings(filename)
#     ddmmyyyy_list = [value.split() for value in date_list]
#     return ddmmyyyy_list
#     # def transform(day):
#
#     return ddmmyyyy_list








# filename = "domains.txt"
# domains_list = create_domains_list(filename)

# filename = "names.txt"
# surnames_list = create_surnames_list(filename)