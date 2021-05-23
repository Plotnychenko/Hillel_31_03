# Homework 9
# E. Plotnychenko

################################################
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


def create_domains_list(filename):
    with open(filename, "r") as txt_files:
        domains_list = txt_files.readlines()
    new_domains_list = [value.lstrip(".") for value in domains_list]
    return new_domains_list

################################################
"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


def create_surnames_list(filename):
    with open(filename, "r") as txt_files:
        object_list = txt_files.readlines()
    strings_split_list = [my_str.split("\t") for my_str in object_list]
    surnames_list = [surname[1] for surname in strings_split_list]
    return surnames_list

################################################
"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""


def create_date_original_list(filename):
    with open(filename, "r") as txt_files:
        info_list = txt_files.readlines()
    info_list = [value.split(" - ")[0].split() for value in info_list if " - " in value]
    date_original_list = [value for value in info_list if len(value) == 3]
    return date_original_list


def modified_date(date):
    date[0] = date[0].rstrip("nsthrd")
    if len(date[0]) == 1:
        date[0] = "0" + date[0]
    date[1] = month_dict[date[1]]
    return "/".join(date)


def create_list_date_dict(filename):
    list_date_dict = []
    date_original_list = create_date_original_list(filename)
    index = 0
    while index < len(date_original_list):
        original_date = " ".join(date_original_list[index])  # В функции create_date_original_list я делаю split по пробелам, из-за этого в этой строчке необходимо заново делать join с пробелом
        dict_date = {"data_original": original_date, "data_modified": modified_date(date_original_list[index])}
        list_date_dict.append(dict_date)
        index += 1
    return list_date_dict


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

filename = "domains.txt"
domains_list = create_domains_list(filename)

filename = "names.txt"
surnames_list = create_surnames_list(filename)

filename = "authors.txt"
date_dict = create_list_date_dict(filename)