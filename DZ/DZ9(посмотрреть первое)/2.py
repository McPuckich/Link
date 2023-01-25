# 2 задание дз 9
studs = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    sname = input(str(i + 1) + "-й студент: ")
    point = int(input("Балл: "))
    studs[sname] = point
    s += point
print(studs)
avrg = s / n
print(avrg)
for i in studs:
    if studs[i] > avrg:
        print(i)