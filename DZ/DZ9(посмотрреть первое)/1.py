zp = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
print(zp['emp3'])
print(zp['emp3']['salary'])
zp['emp3']['salary'] = 8500
print(zp['emp3'])
print(zp['emp3']['salary'])
