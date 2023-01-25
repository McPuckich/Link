s = tuple([input("-> ") for i in range(int(input("Введите длинну кортежа: ")))])
print(s)

for i in s:
    a = s.count(i)
    print(a)
    print("Количество = ", s.count(i))
    if a >= 2:
        break


