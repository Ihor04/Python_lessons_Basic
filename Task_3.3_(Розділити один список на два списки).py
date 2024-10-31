list_for_work = [1, 3, 4, 5, 6]
list_separate = (len(list_for_work) + 1) // 2

first_part_list = list_for_work[:list_separate]
second_part_list = list_for_work[list_separate:]

print(first_part_list, second_part_list)

