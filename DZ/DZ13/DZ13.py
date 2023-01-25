from random import randint

sp = [randint(0, 10) for i in range(5)]
print(sp)

def sred(chis):
    def wrap():
        arif = chis() / len()
        print(arif)
    return wrap

@sred
def summ(a):
    s = 0
    for i in a:
        s += i
    print("Сумма чисел =", s)
    return s


summ(sp)





