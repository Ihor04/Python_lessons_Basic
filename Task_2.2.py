number = int(input("Введіть п'ятизначне число: "))

num_5 = number % 10
num_4 = (number % 100) // 10
num_3 = (number % 1000) // 100
num_2 = (number % 10000) // 1000
num_1 = (number % 100000) // 10000
print(num_5, num_4, num_3, num_2, num_1, sep="")

