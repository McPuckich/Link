a = int(input("Длинна: "))
b = int(input("Ширина: "))
s1 = input("Тип символа 1: ")
s2 = input("Тип символа 2: ")
st = 1

while st <= b:
    if st % 2 == 1:
        print(s1 * a)
    else:
        print(s2 * a)
    st += 1