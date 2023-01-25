# дз с объемом локальная
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a,c) + rect_square(b, c))
#     return s
#
#
# print(rect_paral_square(2,4,6))
# print(rect_paral_square(5,8,2))
# print(rect_paral_square(1,6,8))

# дз с объемом глобальная

s = 0


# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a,c) + rect_square(b, c))
#
#
# print(rect_paral_square(2,4,6))
# print(rect_paral_square(5,8,2))
# print(rect_paral_square(1,6,8))


# дз с объемом не локальная
def rect_paral_square(a, b, c):
    s = 0

    def rect_square(i, j):
        nonlocal s
        s += i * j

    rect_square(a, b)
    rect_square(a, c)
    rect_square(b, c)
    return 2 * s


print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))