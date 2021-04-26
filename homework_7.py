# Homework 7
# E.Plotnychenko

################################################
# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

persons = [
    {"name": "Sheldon", "age": 32},
    {"name": "Leonard", "age": 32},
    {"name": "Penny", "age": 28},
    {"name": "Hovard", "age": 30},
    {"name": "Radj", "age": 28},
]
persons_dict = {}
name_list = []
age_list = []
for person in persons:
    name_list.append(list(person.values())[0])
    age_list.append(list(person.values())[1])
young_person = [name_list[index] for index, age in enumerate(age_list) if age == min(age_list)]
print(young_person)

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
len_name = [len(value) for value in name_list]
long_name = [name_list[index] for index, length in enumerate(len_name) if length == max(len_name)]
print(long_name)
# в) Посчитать среднее количество лет всех людей из списка.
age_sum = 0
for value in age_list:
    age_sum += value
mean_age = age_sum/len(age_list)

################################################
# Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {
    "name": "Andrea",
    "surname": "Bruck",
    "age": "18",
    "phone": "456669874"
}
my_dict_2 = {
    "name": "Den",
    "surname": "Irbis",
    "address": "221b, Baker Street, London",
    "job": "PR manager"
}
# а) Создать список из ключей, которые есть в обоих словарях.
keys_list = [key for key in my_dict_1 if key in my_dict_2]
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
keys_list_1 = [key for key in my_dict_1 if key not in my_dict_2]
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {key: value for key, value in my_dict_1.items() if key in keys_list_1}
"""
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
"""
total_dict = my_dict_1.copy()
for my_key, my_value in my_dict_1.items():
    if my_key in my_dict_2:
        total_dict[my_key] = [my_dict_1.get(my_key)] + [my_dict_2.get(my_key)]
for my_key_1, my_value_1 in my_dict_2.items():
    if my_key_1 not in my_dict_1:
        total_dict[my_key_1] = my_dict_2.get(my_key_1)