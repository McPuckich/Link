x = int(input("Количество символов: "))
s = input("Тип символа: ")
print("0 - горизонтальная \n1 - вертикальная")
o = int(input("Ориентация линий: "))


if o == 0:
    print(s * x)
elif o == 1:
        while x > 0:
            print(s)
            x -= 1