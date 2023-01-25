h = int(input("Выввести треугольник из звёздочек высотой:"))
a = h
for i in range(h):
    print("*" * a)
    a -= 1