# Homework 3
# E. Plotnychenko

################################################

value = int(input("Please, enter an integer: "))
new_value = value / 2 if value < 100 else value * -1
print(new_value)

################################################

value = int(input("Please, enter an integer: "))
new_value = 1 if value < 100 else 0
print(new_value)

################################################

value = int(input("Please, enter an integer: "))
new_value = True if value < 100 else False
print(new_value)

################################################

my_str = input("Please, enter a char or words: ")
print(my_str[1::2])

################################################

my_str = input("Please, enter a char or words: ")
print(my_str[::2])

################################################

my_str = input("Please, enter a char or words: ")

if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)

################################################

my_str = input("Please, enter a char or words: ")

if len(my_str) < 5:
    print(my_str + my_str[::-1])
else:
    print(my_str)