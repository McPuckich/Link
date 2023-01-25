from math import pi, sqrt
print("Выберете операцию:")
print("Вычисление площаи фигур")
print("Выбор фигуры:")
print("1 - треугольник")
print("2 - прямоугольник")
print("3 - круг")


op = int(input("Введите цифру: "))

match op:
    case 1:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        if a > 0 and b > 0 and c > 0:
            if c > a + b or a > c + b or b > a + c:
                print("Такого треугольника не сущуствует")
            else:
                p = (a + b + c)/2
                s = sqrt(p*(p - a) * (p - b) * (p - c))
                print(s)
        else:
            print("Введите положительное число")
    case 2:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        if a > 0 and b > 0:
            s = a * b
            print(s)
        else:
            print("Введите положительное число")
    case 3:
        r = int(input("Введите радиус r: "))
        if r > 0:
            s = pi*(r**2)
            print(s)
        else:
            print("Введите положительное число")


