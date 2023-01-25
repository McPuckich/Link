from random import randint


def maximus(a=117, b=7):
    st = [randint(0, a) for i in range(randint(1, b))]
    print(st)
    for i in range(len(st)):
        a = []
        if st[i] % 13 == 0:
            a.append(st[i])
            return max(a)


x = maximus(229, 8)
c = maximus(65, 1)