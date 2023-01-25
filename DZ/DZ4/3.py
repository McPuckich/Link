a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(a)
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=" ")
