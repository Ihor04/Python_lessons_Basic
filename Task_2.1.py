number = int(input("Введіть 4-значне число: "))

num_1 = number // 1000
num_2 = (number % 1000) // 100
num_3 = (number % 100) // 10
num_4 = number % 10

print(num_1, num_2, num_3, num_4, sep="\n")
