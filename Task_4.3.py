import random

lst = random.randint(3, 10)
random_lst = [random.randint(1, 100) for _ in range(lst)]

new_lst = [random_lst[0], random_lst[2], random_lst[-2]]

print(random_lst, '==', new_lst)
