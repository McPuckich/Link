# name = "Egor"  # имя
# # print("Hello", name)
# # age = 20
# # print(age)
# # print(type(age))
# # print(id(age))
# # age = "hi"
# # print(type(age))
#
# a = b = c = 1, "hi", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type("2.3"))
import random
# a = "5"
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
# # c = a
# # a = b
# # b = c
# # a = a + b # a = 1 + 2 = 3
# # b = a - b # b = 3 - 1 = 1
# # a = a - b # a = 3 - 1 = 2
# a, b = b, a
# print("a =", a)
# print("b =", b)

# print("строка \
# символов")
# print("строка символов строка символов \nстрока символов строка символов "
#       "строка символов строка символов")
# print("\tДокумент       \"file.txt\" D:\\folder\\file.py")

# s1 = "hello"
# s2 = "python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(5464546546546564654)
# print(5.464546546546564654)

# print(6+2)
# print(6-2)
# print(6*2)
# print(7/2)
# print(7//2)
# print(7**2)
# print(7%2)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * 5 ** (2 + 7)
# print(number)

# a = 5
# b = 7
# c = 3
#
# summa = a + b + c
# print("Сумма: ", summa)
# pr = a * b * c
# print("Произведение: ", pr)
# arifnet = summa/3
# print("Среднее арифметическое: ", arifnet)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num -3
# print(num)  # 12

# num = 4321
# a = num % 10
# # print(a)
# num //= 10
# # print(num)
# b = num % 10
# # print(b)
# num //= 10
# # print(num)
# c = num % 10
# # print(c)
# num //= 10
# # print(num)
# d = num % 10
# # print(d)
# num //= 10
# # print(num)
# print(a*1000+b*100+c*10+d)

# num = 4321
# res = num % 10 * 1000
# num //= 10  # 432
# res += num % 10 * 100
# num //= 10  # 43
# res += num % 10 * 10
# num //= 10  # 4
# res += num % 10
# print(res)

# Функция явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = int(float(num1)) + num2
# print(res)
#
# print(int(3.8))
# a = round(3.8)
# print(a)
# print(type(a))
# b = round(3.891, 2)
# print(b)
# print(type(b))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end="")
# print("Я учу Python")

# name = input("Ваше имя: ")
# print(name)

# Число 5 в степени 2 равно 25
# num = int(input("Введите число: "))
# step = int(input("Введите степень: "))
# res = num ** step
# print("Число:",num,"в степени:",step,"равно:",res)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool(5))
# print(bool(0))
# print(bool(False))
# print(bool(None))
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(8 != 7)
# print(3 + 5 >= 7)
# print(5 <= 7)
# print(5 < 7)
# print(9 > 7)

# print(8 > 4 > 9)  # True && False
# print(3 * 3 <= 7 >= 2)  # False && True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 3 + 1 == 4)  # True (True:True)
# print(5 - 3 == 2 and 3 + 1 < 4)  # False (True:False)

# print(5 - 3 == 2 or 3 + 1 == 4)  # True (True:True)
# print(5 - 3 == 2 or 3 + 1 < 4)  # True (True:False)

# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 45
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Введите значение первой стороны: "))
# b = int(input("Введите значение второй стороны: "))
# c = int(input("Введите значение третьей стороны: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели нет")

# m = int(input("Введите день недели (цифрой): "))
# if 1 <= m <= 2 or m == 12:
#     print("Winter")
# elif 3 <= m <= 5:
#     print("Spring")
# elif 6 <= m <= 8:
#     print("Summer")
# elif 9 <= m <= 11:
#     print("Autumn")
# else:
#     print("Такого месяца не существует")

# v = int(input("Введите количество ворон на ветке (от 0 до 9): "))
# if 0 <= v <= 9:
#     print("На ветке", v, end="")
#     if v == 1:
#         print("ворона")
#     elif 2 <= v <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода")

# password = "moderator"

# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = 'суббота'
# time = 8
# match day:
#     case 'понедельник'| 'вторник' | 'среда' | 'четверг' | 'пятница' \
#         if 9 <= time <= 16:
#         print('рабочий день')
#     case 'суббота'| 'воскресенье':
#         print('рабочий день')
#     case _:
#         print('Такого дня недели не существует')

# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 30, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 10, 0
# print(a/b if b!= 0 else "На ноль делить нельзя")

# Исключения

# a = 5
# b = "0"
# print(a / b)


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Что-то пошло не так")
#     print("Нельзя делить на ноль")
# else:  # выполняется когда в блоке Try не воникло исключения
#     print("Всё нормально. Вы ввели верные числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#    n = int(n)
#    m = int(m)
# except ValueError:
#     s = str(n)
# finally:
#     print(n + m)

# Циклы

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2
#
# i = 1
# while i <= 10:
#     print(i * 2, end=" ")
#     i += 1
#
# i = 2
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#         i += 1

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#         print('*', end='')
#         x -= 1
# except ValueError:
#     print('Введите число!')


# x = int(input('Количество: '))
# i = 0
#     while i < x:
#         print('*', end='')
#         i += 1
# except ValueError:
#     print('Введите число!')

# x = int(input("Введите число: "))
# i = 0
# string = ""
# while i < x:
#     string += "*"
#     i += 1
# print(string)

# x = int(input("Количество знаков: "))
# print("*" * x)

# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# summa = 0
# while a <= b:
#     summa += a
#     a += 2;
# print('Сумма нечетных: ', summa)

# i = int(input("Start: "))
# j = int(input("End: "))
# sum1 = 0
# while i <= j:
#     if i % 2 != 0:
#         sum1 += i
#     i += 1
#
# print(sum1)

# n = input('Введите число: ')
#
# while  type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i +=1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += i

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# m = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     m *= n
# print("Произведение равно: ", m)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += i
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", i)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

# range(start, stop, step)

# for i in range(10, 0,-1):
#     print(i, end=" ")
#
# # аналог примера через while
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(3):
#     print(i, end=" ")
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print("\ndone")

# for i in range(3):
#     print("***", i)
#     for j in range(2):
#         print("-----", j)

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if 0 < i < h - 1 and 0 < j < w - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)

# nums = [8, 3, 9, 4, 1, "hello", 2.3]
# print(nums)
# print(type(nums))
# print(id(nums))
# print(nums[0])
# print(nums[-1])
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(id(nums))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# с = list("hello")
# print(с)

# s = [5, 2] * 6
# print(s)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# n = list(range(2, 10, 2))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
#
# for i in range(len(nums)):
#     print(nums[i], end=" ")
# print()
# for i in nums:
#     # print(i * 2, end=" ")

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa=0
# for i in a:
#     if i<0:
#         summa+=i
# print(summa)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += 1
# print('Четных: ', odd, '\nНечетных: ', even)

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
# count = sum1 = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum1 += i
# print('Среднее: ', sum1 / count)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов списка: ")))]
#
# b = a[0]
#
# for i in a:
#     if i > b:
#         print(i, end=" ")
#     b = i


# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)
#
#
# # список[start:stop:step]
#
# a = [9, 4, 3, 1, 5, 17]
#
# print(a[1:4])
# print(a[1:])
# print(a[:])


# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])

# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:3] = [20]
# print(a)
# a[2] = [50]
# print(a)
# a[3:5] = []
# print(a)
# del a[:]
# print(a)

# Методы списков
# print(dir(list))

# a = list(range(1, 8))
# print(a)
# a.append(99)  # добавляет один жлемент в конец списска (как значение, так и список)
# print(a)
# a.extend([22, 11, 9])  # добавляет множество элементов в конец списка
# print(a)
# a.insert(-1, 100)  # добавляет элемент в список . Первый параметр индекс. Второй параметр добавляемое значение
# # смещает значение вправо
# print(a)
# a.extend("add")
# print(a)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = input("--> ")
#     s.append(x)
# print(s)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("--> "))
#     if x % 3 == 0:
#         print("Введите чиссло кратное 3: ", x)
#         s.append(x)
#     else:
#         print(x, "Не делитсся на 3")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 2, 4]
# c = []
#
# # if len(b) < len(a):
# #     a, b = b, a
# # for i in range(len(a)):
# #     c.append(a[i])
# #     c.append(b[i])
# # for i in range(len(a), len(b)):
# #     c.append(b[i])
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 13, 12, 13, 2, 4, 13]
# b.remove(13)  # удаляет элемент из списка по значению, если элементов с заданным значением несколько,
# # то удаляется первый.
# print(b)
# a = 3
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # с пустыми скобками удаляет последний элемент из списка, с заданным индексом в скобках
# # удаляет по индексу
# print(b)
# print(last)
#
# b.clear()  # очищает список от всех элементов
# print(b)

# a = [int(input('-> ')) for num in ' ' * int(input('Count: '))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)  # Количесство заданных значений в списке
# print(a)
# print(num)
# ind = a.index(2, 2, -1)  # Возвращает первый индекс искомого значения. Также можно узнать значения начала
# # и конца списка
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a:", a)
# print("b:", b)
# a.append(20)
# b.remove(9)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# a.reverse()  # перестраивает элемениты списска в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортирует список, по умолчанию - по возрастанию, reverse=True - по убыванию
# print(a)
#
# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
#
# c = sorted(a)
# print(c)
# print(a)

# Генерация случайных чисел

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # от 2 до 9 (включительно)
# print(random.randrange(2, 9, 2))

# from random import randint, randrange
#
# print(random.randint(2, 9))
# print(random.randrange(2, 9, 2))

# from random import *
#
# print(random.randint(2, 9))
# print(random.randrange(2, 9, 2))

# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(2, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))

# city = ["Москва", "Новоссибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # city = [5, 3, 9, 7, 8, 6, 4, 2, 1]
# # print(r.choice(city))
# # print(r.choices(city, k=5))
# r.shuffle(city)
# print(city)

import random as r

# mas = [r.randint(30, 100) for i in range(5)]
# print(mas)

# sum = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
# print(res)

# x = list('1a2b3c4c')
# print(x)
# print('a' in x)
# print('w' in x)
# print('w' not in x)
# print('a' not in x)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(a)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторения", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие обоих списков", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# import random
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)
#
# from random import randint

# a = []
# n1 = int(input('Введите размер первого списка'))
# while len(a) < n1:
#     i = randint(0, n1 - 1)
#     if i not in a:
#         a.append(i)
# print(a)

# from random import randint
#
# n = int(input("Количество элементов списка: "))
# a = [randint(0, n - 1)]
# while len(a) < n:
#     c = randint(0, n - 1)
#     if c not in a:
#         a.append(c)
# print(a)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# print(m)
# print(m[2][2])
#
# for row in range(len(m)):
#     print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# Вложенные списки

# w, h = 5, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# # print(matrix)
# matrix = []
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):  # 5
#         new_row.append(0)
#     matrix.append(new_row)
# #
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# print([[x for x in row] for row in matrix])

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
# a= [[1, 2], [3, 4], [5, 6], [7, 8]]
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# from random import randint
#
# w, h = 3, 4
# matrix = [[ randint(-20, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# from random import randint
#
# w, h = 3, 4
# count = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#         if x < 0:
#             count += 1
#     print()
# print('Количество отрицательных чисел:', count)
#
# from random import randint

# w, h = 3, 4
# n = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x != 0:
#             n *= x
#         print(x, end='\t\t')
#     print()
# print('n=', n)

# from random import randint
#
# w, h = 3, 4
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# s = []
# m = 101
# for i in range(w):
#     s.append()
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(m)
# print(min(s))

# import math
# from math import sqrt, ceil, floor, pi
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# # r = int(input("Радиус: "))
# # print("Длинна окружности", round(2*pi*r, 2))
# import math
# print(round(int(input("Введите радиус окружности: ")) * 2 *math.pi, 2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# # print(time.strftime("today is %B %d, %Y"))
# print(time.strftime("%d/%m%Y, %H:%M:%S", time.localtime(4654414541)))
# print(time.strftime("Сегодня: %B %d, %Y"))

# import time
# import locale
#
# pause = 5
# print("Programm started...")
# time.sleep(pause)
# print(pause, "seconds")

# import time
# import locale
#
# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# import time
# import locale
#
# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")


# Функции
# a = 2
# #
# #
# # def hello(name, word):
# #     print("Hello", name, ". Say", word, sep="")
# #
# #
# # hello("Irina", "hi")
# # hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#     print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print("Строка")
#     return a + b
#
#
# x = 2
# y = 5
# w = get_sum(x, y)
# print(w * 2)

# def get_sum(a, b):
#     print(a + b)
#     return
#
#
# x = 2
# y = 5
# get_sum(x, y)

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if  "a" <= ch <= "z":
#             has_lower = True
#         if  "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     # end = lst.pop()
#     # start = lst.pop(0)
#     # lst.insert(0, end)
#     # lst.append(start)
#     # return lst
#     return [lst[-1]] + lst[1:-1] + [lst[0]]
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))
#
# print([3] + [2, 4] + [1])

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# w = 5
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5))
# print(get_sum(1, 2, d=w))

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_dight = n % 10
#         if even and cur_dight % 2 == 0:
#             s += cur_dight
#         if not even and cur_dight % 2 != 0:
#             s += cur_dight
#         n //= 10
#     return s
#
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info('Igor', age=23, name="Ira")

# Изменяемые и не изменяемые объекты

# lt1 = [1,2, 3]
# lt2 = [1,2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)

# lt1 = [1,2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))

# s = "Hello"
# print(id(s))
# s += "world"
# print(s)
# print(id(s))

# Кортеж (tuple)

# lst = [10,20, 30]
# tpl = (10,20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# b = tuple(a)
# print(type(b))
# print(b)

# t = 2,
# print(type(t))
# print(t)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple([input("-> ") for i in range(3)])
# print(s)

# s = input("-> ")
# print(tuple(s))

# from random import randint
#
# s = tuple(1, 30) for i in range(20)
#
#
#     s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
#
# print(t3.index('l'))
# print(t3.index('a'))
# print(t3.index('l', 3))
#
# print(t3.count('l'))
# print(t3.count('a'))
#
# print(t3.index('l', 4))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")
#
# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first: second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el)+ 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if not num in tup:
#         return tuple()
#     first = tup.index(num)
#     if not num in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def tpl_sum(t1, t2):
#     print(t1)
#     print(t2)
#     print(t1 + t2, (t1 + t2).count(0))
#
#
# tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for i in range(12)))
#
# from random import randint
#
#
# def tpl_sum(a, b):
#     return tuple(randint(a, b) for _ in range(12))
#
#
# t1 = tuple((0, 5) for i in range(12))
# print(t1)
# t2 = tuple(randint(-5, 0) for j in range(12))
# print(t2)
# print(t1 + t2, (t1 + t2).count(0))


# =================================

# point = (0, 0)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси Х и в коорденате 0 по оси Y")
#     case (0, y):
#         print("Точка находится в координате 0 по оси X и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси Х и в коорденате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = [2, 3]
# print("t =", id(t))
# print(id(t[0]))
# t[0] = 5
# print(t)
# print(id(t[0]))
# print("t =", id(t))

# t = (10, 11, [1,2,3], [4,5,6],["hello", "world"])
# print(t, id(t))
# print(len(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))
# print(len(t))

# a = list(range(2))
# print(a)
# print(a.__sizeof__())
# b = list(range(1))
# print(b)
# print(b.__sizeof__())

# Распаковка картежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# name1, age1, married1 = user
# print(user)
# print(name1, age1, married1)
#
#
# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)
#
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# print()
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     # print(country)
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)
#

# list() список изменяемый тип данных
# tuple() кортеж не изменяемый тип данных
# set() множество(в нём храниться неупорядоченная коллекция уникальных данных) изменяемый тип данных
# frozenset()

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# a = set('hello')
# print(type(a))
# print(a)

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = {x for x in numbers if x % 2 == 0}
# print(s)


# def to_set(par):
#     return (set(par), len(set(par)))
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r}
# c = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:] )
#         else:
#             print("B" + i[1:])


# s = {'banana', 'apple', 'orange'}
# # s.add(4)  # добавляет элемент во множество
# # if 44 in s:
# #     s.remove(44)  # удаляет элемент по значению
# # s.discard(44)  # удаляет элемент по значению без генерации исключения
# a = s.pop()  # удаление первого элемента из множества
# s.clear()  # полностью удаляет множество
# print(s)
# print(a)


# Операции над множествами
# a = {0, 1, 2, 3, 4}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# c = a & b
# a |= b
# a &= b
# c = a - b
# a -= b
# c = a ^ b
# a ^= b
# c = a >= b
# # print(c)
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = "Hello"
# s2 = "How are you"
# print(set(s1) & set(s2))
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")

# s1 = "Python"
# s2 = "Programming language"
# print(set(s1) & set(s2))

# s1 = "Python"
# # s2 = "Programming language"
# # print(set(s1) - set(s2))
# #
# # a = "Python"
# # b = "Programming language"
# # c = set(a) - set(b)
# # for i in c:
# #     print(i, end=" ")
# # print(set(s1) - set(s2))

# drawing = {"Маринна", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
# drawing = drawing - both_hobby
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({"Hello", "world"})
# print(s1)


# Словарь (dict) коллекция данных представляющая собой набор ключей (изменяемый тип данных)

# a = [1, 2, 3]
# d = {1: 'one', 'two': 2, 'three': 3, 'four': 3}
# print(a[0])
# print(d['one'])
# print(d[1])
#
#
# d = {}
# print(d)
# print(type(d))


# d = dict()
# print(d)
# print(type(d))

# d = {"one": 1, "two": 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))


# a = [
#     ("igor@gmail.com", "Igor"),
#     ("irina@gmail.com", "Irina"),
#     ("anna@gmail.com", "Anna")
# ]
#
# b = dict(a)
# print(b)


# d = {i: i ** 2 for i in range(2, 7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)


# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", (2, 3, 6, 7): 42, True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("one" in d)
# print(d["one1"])
#
# key = 'one'
# # if key in d:
# #     del d[key]
# # print(d["one1"])
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + "нет в словаре")
#
# print(d)

# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, "-> ", d[key])


# some_dict = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# summator = 1
# for key in some_dict:
#     summator *= some_dict[key]
# print(summator)


# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)
# d = {i: input("-> ") for i in range(1, 5)}
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }

# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != "0":
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по", goods[i][2], "руб", sep="")


# d = {'a': 1, 'b': 2,  'c': 3}
# print(d['c'])
#
# value = d.get('f', False)  # Получить значение по заданному ключу
# print(value)
# n = d.keys()  # спиок ключей
# print(n)
# n = d.values()  # спиок значекний
# print(n)
# n = d.items()   # спиок кортежей ключ + значение
# print(n)
#
# for i, j in d.items():
#     print(i, "->", j)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d
#
# print("D =", d)
# print("D2 =", d2)
#
# d['b'] = 5
# d['e'] = 7
#
# print("D =", d)
# print("D2 =", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')  # удаляет элемент из словоря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem('c')  # удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)
# item = d.setdefault('f', 5)  # добавляет ключ со значением по умолчаниюб если ключа не существует
# print(item)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d.update({'a': 20, 'w': 10})
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'c': 3, 'd': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NEw York'}
#
# # new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
#
# # new_d = {'name': d.pop('name'),'salary': d.pop('salary')}
# # print(d)
# # print(new_d)
#
# d['location'] = d.pop('city')
# print(d)

# a= {
#     'first': {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     'seond': {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# w = {k: v for k, v in d.items() if v <= 2}
# print(w)
#
# value =
#
# c
# count = 0
# for i in d:
#     print(i, ":", d[i])
#     count += 1
#     if count == 2
#         break

# value = int(input("-->"))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2,'c': 3,'d': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     some_list = list()
#     if type(i) == str:
#         d[i] = []   # d["one"] = []
#         s = i   # s = "one"
#     else:
#         d[s].append(i)
#
# print(d)


# a = {"Dec", "Jan", "Feb"}
# b = {12, 1, 2}
# d = list(zip(a, b))
# print(d)


# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
# d = list(zip(a, b, c))
# print(d)


# one = {"name": "Igor", "last_name": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "last_name": "Smith", "job": "Manager"}


# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# one = {{"name": "Igor", "last_name": "Doe", "job": "Consultant"},
#        {"name": "Irina", "last_name": "Smith", "job": "Manager"}
#        }
# print(one)

# pairs = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
# a, b = zip(pairs)
# print(a)
# print(b)


# one = {"apple": 0.4, "orange": 0.35}
# two = {"pepper": 0.2, "onion": 0.55}
# print({one, two})


# data = ["a", "b", "c", "d"]

# for i in data:
#     print(i, end=" ")
# print()
# for i in range(len(data)):
#     print(i, end=" ")
#
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 100):
#     print(j, ":", i)

# n = {"a": 1, "b": 2, "c": 3, "d": 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ":", i, "->", v)


# a = [1, 2, 3]
# b = [4,a, 5, 6]
# print(b)
#
#
# def func(*args):
#     res = 0
#     for i in args:
#         res += 1
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6))
# print(func())

# def to_dict(*lst):
#     print(*lst)
#     print(lst)
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2,17), 3.11, -4))


# мой вариант
# def sred(*chi):
#     for i in chi:
#         sum += i
#         print(sum)
#     if i < sum:
#
#
# print(sred(1,2,3,4,5,6,7,8,9,))


# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))


# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ',avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)
#
#
#
# print(func(3, 6, 1, 9, 5))
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(2, 3))
# print(func(2,3,4, 'abc'))


# def print_scores(student, *scores):
#     print("\nstudent name", student, end=", scores: ")
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#
#
# print_scores("kate", 100, 95, 88, 92, 99)
# print_scores("rick", 96, 20, 33, 56)

# def print_scores(student, *scores):
#     print("\nStudent Name:", student, end=", scores: ")
#     count = 0
#     for score in scores:
#         count += 1
#         if count!= len(scores):
#             print(score, end=", ")
#         else:
#             print(score)
#
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)

# def revers_num(n):  # 12 => 21
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2):
#             res.append(revers_num(i))
#     return res
#
# print(func(12,2345,323,4456,5687,62,734,81,91))
# print(func(12,2345,323,4456,5687,62,734,81,91, only_add=True))


# def func(**kwargs):
#     return
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))


# def func(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))
#
#
# func(name="Irina", surname="Sharma", age=22, phone=1234567890)
# func(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=9876543210)


# def func(**data):
#     # for key, value in data.items():
#     #     my_dict[key] = value
#     # return my_dict
#     my_dict.update(**data)
#
#
# my_dict = {'one': 'first'}
# print(func(k1=22, k2=31, k3=11, k4=91))
# print(my_dict)
# print(func(name='Bob',age=31,weight=61,eyes_color='grey'))
# print(my_dict)

# def func(a, *args, b=2, **kwargs):
#     print(a, args, kwargs, b)
#
#
# func(4, 5, 6, 7, b=3, k1=22, k2=31, k3=11, k4=41)

# Области видимости (scope)

# name = "Tom"    # глобальная переменная
#
#
# def hi():
#     global name, surname
#     name = "Sam"    # локальные переменные
#     surname = "Johnson"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name, surname)
#
#
# hi()
# print(surname)
# bye()


# i = 5
#
# def func(arg=i):
#     print(arg)
#
#
# i=6
# func()  # 5


# x = 5
#
# def add_two(a):
#     # x = 2
#
#     def add_some():
#         # x = 3
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))
# print(x)


# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)
#


# max = [8, 1, 1, 2,, 4, 5, 6, 9]  # не задавай имена переменным через функции
# print(min(max))
#
# a = [7, 8, 9, 5]
# print(max(a))

# def outer_func(who):
#     def inner_func():
#         print("hello", who)
#
#     inner_func()
#
#
# outer_func("world!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()
#
# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)
#
#
# a = 12
# a = ""
# print(a)

# def fun1():
#     x = 25
#
#     def fun2():
#         x = 33
#
#         def fun3():
#             nonlocal x
#             x = 55
#
#         fun3()
#         print("fun2.x", x)
#
#     fun2()
#     print("fun1.x", x)
#
#
# fun1()
# print(x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner

# add = outer(5)
# print(add(10))
# print(add(20))
#
# add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + ", hine"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


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
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Gracce': 69
# }
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A = ", A(students))
# print("B = ", B(students))
# print("C = ", C(students))
# print("D = ", D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print("qqqqqqq")
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.mul())
# print(obj1.sub())
# obj1()
#
# max = 5
# max([4, 5, 6, 4])

# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# a = 5
# func = lambda x, y: x + y + a
#
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x**2 + y**2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c

# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
#
# print(func(1,2,3,4,5,6,7))
# print(func(1,2))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
#
# inc1 = (lambda  n: lambda x: n + x)
#
# f3 = inc1(42)
# print(f3(3))
#
#
# print("!!!",(lambda  n: lambda x: n + x)(42)(3))
#
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap
#
#
# f1 = inc2(42)
# print(f1(3))


# print("!!!",(lambda  n: lambda x: lambda j: n + x + j)(42)(3)(2))

# players = [
#     {'name': 'Антон', 'lust name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'lust name': 'Бодня', 'rating': 10},
#     {'name': 'Федоров', 'lust name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'lust name': 'Семенов', 'rating': 6},
# ]
#
#
# res = sorted(players, key=lambda item: item['lust name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse = True)
# print(res)


# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i:i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x + y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print((a[3](12, 3)))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[3]()

# print((lambda a,b:a if a>b else b)(12, 5))
#
# m = lambda a, b, c: a if a < b else b if b < c else c
# print(m(19, 28, 25))
#
# print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 8, 5))


# map(func, iterable), filter() (func-функция interable-итеранд)


# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)


# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x:int(x),t))
# t2 = tuple(map(int, t))
#
# print(t2)


# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
#
# res = list(map(round, area, range(1, 7)))
# res2 = list(map(round, area, [2, 2, 2, 2, 2, 2]))
#
#
# print(res)
# print(res2)


# print(round(3.45612131,3))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)
# # res2 = dict(map(lambda x, y: (x, y), st, num))
# # print(res2)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)

# lst = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda elem: elem *lst.index(elem) ** 3, lst)))

# filter(func, iterable)

# t = ('abcd' , 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90,68,59,76,60,88,74,81,65]
# res = list(filter(lambda s: s> 75,b))
# print(res)

# from random import randint
#
# b = [randint(0, 50) for i in range(10)]
# print(b)
# res = list(filter(lambda s: s >= 10 and s <= 20, b))
# print(res)

# nums = [45,55,60,37,100,105,220]
# res = list(filter(lambda x: x%15==0 ,nums))
# print(res)

# m = list(map(lambda x: x**2, filter(lambda x: x % 2, range(10))))
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, i am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, i am func "func_test"')
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count +=1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     return "Hello"
#
#
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", last="Назарова", second="Федорович")

# def decor(*args):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args[0], x, args[1], y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", **f_args[i])
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", **f_kwargs[k])
#
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return (x + y) * z
#
# @typed(str, str, z = int)
# def typed_fn3(x, y, z):
#     return x + y + z
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2('hello', 'world', '!'))
# print(typed_fn3('hello', 'world', z = 5))


# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello,")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")
#
# def a(x, y=0):
#     print(y)
#
# a(y=5)

# filter(func, iterable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# z = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda a: 10 < a <= 20, z))
# print(res)


# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)

# nums = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, nums))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # (1, 3, 5, 7, 9)
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Назарова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", last="Назаров", second="Федорович")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
#
# def decor(*args):
#     def args_dec(fn):
#         def wrap(x, y):
#             # print(args[0], x, args[1], y, "=", end=" ")
#             print(*args, end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(ch):
#     return ch
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", f_args[i])  # print("Некорректный тип данных!")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))


# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")

print("hi")