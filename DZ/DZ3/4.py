print("Выберете операцию:")
print("1 - 'r' - применение унарного минуса к операнду")
print("2 - '+' - сложение")
print("3 - '-' - вычитание")
print("4 - '/' - деление")
print("5 - '*' - умножение")
print("6 - '%' - деление по модулю (остаток от деления)")
print("7 - '<' - минимальное из двух чисел")
print("8 - '>' - максимальное из двух чисел")

op = int(input("Введите цифру: "))
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

match op:
    case 1:
        x = x * (-1)
        print(x)
    case 2:
        s = x + y
        print(s)
    case 3:
        s = x - y
        print(s)
    case 4:
        try:
            s = x / y
            print(s)
        except ZeroDivisionError:
            print("Нельзя делить на ноль")
    case 5:
        s = x * y
        print(s)
    case 6:
        s = x % y
        print(s)
    case 7:
        s = x if x < y else y
        print(s)
    case 8:
        s = x if x > y else y
        print(s)
