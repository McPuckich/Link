a = [int(input("Число: ")) for i in range(int(input("Диапазон")))]

for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")

