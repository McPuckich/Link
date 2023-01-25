v = int(input("Введите количество копеек (от 1 до 99): "))
if 0 <= v <= 99:
    print(v, end="")
    if v % 10 == 1 and v != 11:
        print(" копейка")
    elif 2 <= v <= 4 or 2 <= v % 10 <= 4 and v > 14:
        print(" копейки")
    else:
        print(" копеек")
else:
    print("Ошибка ввода")


