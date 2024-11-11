lst = [1, 3, 5]

if len(lst) == 0:
    result = 0
else:
    index_sum = sum(lst[::2])
    result = index_sum * lst[-1]

print(result)
