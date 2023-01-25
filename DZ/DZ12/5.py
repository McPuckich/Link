
a = [3, 6, 8, 9, 1, 2]
print(a)
print(list(map(lambda elem: elem *a.index(elem) ** 3, a)))