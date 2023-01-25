stud = [{'name': 'Jenifer', 'final': 95},
        {'name': 'David', 'final': 92},
        {'name': 'Nikolas', 'final': 98}]

# 3 задание
print(stud)
print(sorted(stud, key = lambda student: student["name"]))
print(sorted(stud, key = lambda student: student["final"], reverse = True))
# 4 задание
print(max(stud, key = lambda student: student["final"]))
print(min(stud, key = lambda student: student["final"]))