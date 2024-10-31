
number1 = float(input("Введіть перше число: "))
operation = input("Оберіть дію : +, -, *, / : ")
number2 = float(input("Введіть наступне число: "))

if operation == '+':
    result = number1 + number2
    print("Результат =", result)

elif operation == '-':
    result = number1 - number2
    print("Результат =", result)

elif operation == '*':
    result = number1 * number2
    print("Результат =", result)

elif operation == '/':
    if number2 == 0:
        print("Не ділиться на нуль!")
    else:
        result = number1 / number2
        print("Результат =", result)
