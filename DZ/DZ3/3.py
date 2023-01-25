a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
maximum = c if a < b < c or b < a < c else b if a < c < b or c < a < b else a
print("Максимальное значение", maximum)
