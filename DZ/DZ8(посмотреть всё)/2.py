tpl = ('ab', 'abcd', 'cde', 'abc', 'def')


def fnd(x):
    for i in range(len(tpl)):
        if x == tpl[i]:
            print("yes")
            break
        else:
            print("no")



s = "abcd"
print(s)
fnd(s)

