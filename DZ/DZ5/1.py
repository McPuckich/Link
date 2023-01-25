from random import randint
a = [randint(1, 50) for i in range(10)]
print(a)
maxim = max(a)
print("Max: ", maxim)
poz = a.index(max(a))
b = a.pop(poz)
a.insert(0, b)
print(a)