import random as r

mas = [r.randint(-20, 20) for i in range(10)]
print(mas)
mas.sort(reverse=True)
print(mas)