from random import randint

w, h = 6, 6
matrix = [[randint(0, 11) for x in range(w)] for y in range(h)]
print(matrix)

for y in range(h):
    if y % 2 == 1:
        a = matrix.pop(y)
        matrix.insert(y-1, a)
print(matrix)
