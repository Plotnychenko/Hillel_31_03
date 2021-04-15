# Homework 5
# E.Plotnychenko

################################################

number = 10101010011100
symbol = "0"
result = str(number).count(symbol)

################################################

number = 1002300000
new_number = str(number).rstrip("0")
result = len(str(number)) - len(new_number)

################################################

my_list_1 = [1, 3, 4, "a", "()", 4.55, 123, "asdf"]
my_list_2 = [1, 3, 4, "a", "()", 4.55, 123, "asdf"]
my_result = []
my_result.extend(my_list_1[1::2])
my_result.extend(my_list_2[::2])
print(my_result)

################################################

my_list = [1, 3, 4, "a", "()", 4.55, 123, "asdf"]
new_list = my_list[1:] + my_list[:1]

################################################

my_list = [1, 3, 4, "a", "()", 4.55, 123, "asdf"]
my_list.append(my_list.pop(0))
print(my_list)

################################################

my_str = "24 agasf 31 sad 15 bad  1 asdad 44 qwe"
result = 0
for value in my_str.split(" "):
    if value.isdigit():
        result += int(value)
print(result)

################################################

my_string = "Long string. Very long string."
l_string = "n"
r_string = "n"
sub_string = my_string[my_string.lower().find(l_string) + 1:my_string.lower().rfind(r_string)]

################################################

my_str = "qwerqtqfak1231askda"
my_list = []
if len(my_str) % 2:
    my_str += "_"
index = 0
while index < len(my_str):
    my_list.append(my_str[index:index + 2])
    index += 2

################################################

my_list = [2, 4, 1, 5, 3, 9, 0, 7, 8, 2, 11, 15, 1]
index = 0
count = 0

while index < len(my_list) - 2:
    index += 1
    if my_list[index - 1] + my_list[index + 1] > my_list[index]:
        count += 1
print(count)