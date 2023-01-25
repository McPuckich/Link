from random import randint

w, h = 6, 6
matrix = [[randint(0, 11) for x in range(w)] for y in range(h)]
print(matrix)
st = [randint(0, 11) for x in range(w)]
print(st)
for y in range(h):
    if y % 2 == 0:
        matrix[y] = st
print(matrix)
