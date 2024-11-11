
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result_lst = []

for n in lst:
    if n != 0:
        result_lst.append(n)

for i in range(len(lst) - len(result_lst)):
    result_lst.append(0)

print(result_lst)
