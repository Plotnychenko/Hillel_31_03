# Homework 4
# E.Plotnychenko

################################################

my_list = [1, 4, 6, 99, 102, 100, 65425, 555, 914, 113]

for value in my_list:
    if value > 100:
        print (value)

################################################

my_list = [1, 4, 6, 99, 102, 100, 65425, 555, 914, 113]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print (my_results)

################################################

my_list = [1, 4, 6, 99, 102, 100, 65425, 555, 914, 113]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

################################################

my_string = "0123456789"
results_list = []
for char_1 in my_string:
    for char_2 in my_string:
        results_list.append(int(char_1 + char_2))
        results_list.sort()
print(results_list)
