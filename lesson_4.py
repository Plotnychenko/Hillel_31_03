# Кортежи (tuple) и списки (list)

# my_t = (1, 2, 3, 3.14, "tuple") # Кортеж (tuple)
# my_l = [1, 2, 3, 3.14, "list"] # Список (list)
#
# print(my_t, type(my_t))
# print(my_l, type(my_l))
#
# new_t = tuple(my_l)
# new_l = list(my_t)
#
# print(new_t, type(new_t))
# print(new_l, type(new_l))
#
# print(my_t[0], my_l[0])
# print(my_t[-1], my_l[-1])
# print(my_t[2:5:2], my_l[2:5:2]) # срез кортежа - кортеж, срез списка - список
#
# # Кортежи и списи являются итерируемыми объектами
# # Кортеж - НЕИЗМЕНЯЕМЫЙ ОБЪЕКТ
# # Список - ИЗМЕНЯЕМЫЙ ОБЪЕКТ
# index = 4
# value_t = my_t[index]
# print(value_t)
#
# print(my_l)
# my_l[0] = "test"
# print(my_l)
#
# print(my_t)
# my_t[0] = "test" # ОШИБКА
# print(my_t)
# my_list = [[1, 2], my_l]
# print(my_list, my_list[1][3])
#
# my_tuple = ([1, 2], my_list)
# my_tuple[0][0] = "test" # Если в кортеже есть список(вложенная структура),то сам список внутри кортежа можно изменить
# print(my_tuple)
# new_list = [1] * 3
# new_list_1 = [[1], [2], "test"] * 3
# print(new_list)
# print(new_list_1)
#
# test_list = [1, 2, 3]
# new_test_list = [test_list] * 3
# test_list[-1] = "test"
# print(test_list)
# print(new_test_list)
#
# test_list = [1, 2, 3]
# new_test_list = [test_list.copy()] * 3
# test_list[-1] = "test"
# print(test_list)
# print(new_test_list)

# Добавление в конец списка

# my_list = []
# my_list.append("a")
# my_list.append("vf")
# print(my_list)
# # Удаление с конца списка (убирает последний элемент списка)
# my_list.pop()
# print(my_list)
#
# # Приведение типа - строка в список
# test_list = list("qwerty")
# print(test_list)
# test_list[1] = "W"
# print(test_list)
#
# # Приведение типа - список в строку (только список СТРОК)
#
# new_str = "".join(test_list) # Впереди перед методом стоит склеивающий символ (АБСОЛЮТНО ЛЮБОЙ)
# print(new_str)

# Циклы

# my_list = ["q", "a", 3, 12]
#
# for value in my_list:
#     print(value)
