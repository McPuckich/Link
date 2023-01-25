from random import randint
a = [randint(1, 50) for i in range(10)]
print(a)
minum = min(a)
print("Min: ", minum)
poz = a.index(min(a))
print("Index min", poz)
a[0:poz] = []
print(a)
