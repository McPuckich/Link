from random import randint
a = int(input("Ваше число от 1 до 100: "))
hid = randint(1, 100)
n = 0


while a != hid:
    if a == 0:
        print("Игра окончена")
        break
    if a != 0:
        if a > hid:
            print("Ваше число больше")
            n += 1
            a = int(input("Ваше число от 1 до 100: "))
        if a < hid:
            print("Ваше число меньше")
            n += 1
            a = int(input("Ваше число от 1 до 100: "))
        if a == hid:
            n += 1
            print("Вы угадали число с ", n, " раза")
            break