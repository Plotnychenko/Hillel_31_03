# Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {
    "name": "Andrea",
    "surname": "Bruck",
    "age": "18",
    "phone": "456669874",
    "married": "Yes"
}
my_dict_2 = {
    "name": "Den",
    "surname": "Irbis",
    "address": "221b, Baker Street, London",
    "job": "PR manager",
    "married": "No",
    "children": "No"
}
"""
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
"""
total_dict = my_dict_1.copy()
keys_set = set(my_dict_1.keys()) | set(my_dict_2.keys())
for key in keys_set:
    if key in my_dict_1 and key in my_dict_2:
        total_dict[key] = [my_dict_1.get(key)] + [my_dict_2.get(key)]
    elif key in my_dict_1 and key not in my_dict_2:
        total_dict[key] = my_dict_1.get(key)
    elif key in my_dict_2 and key not in my_dict_1:
        total_dict[key] = my_dict_2.get(key)
print(total_dict)