number = int(input("Введіть п'ятизначне число: "))

num_5 = number % 10
num_4 = (number % 100) // 10
num_3 = (number % 1000) // 100
num_2 = (number % 10000) // 1000
num_1 = (number % 100000) // 10000
output = ((num_5 * 10000) + (num_4 * 1000) + (num_3 * 100) + (num_2 * 10) + num_1)
print(output)
