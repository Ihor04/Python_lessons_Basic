#my_list = []
#my_list = [783]
my_list = [22, 45, "A", 760, "10 - F", True]

if len(my_list) <= 1:
    print(my_list)
else:
    print([my_list[-1]] + my_list[:-1])
