def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1

    if '9' == str(x)[0]:
        return f(x + 1, y)

    if '9' == str(x)[1]:
        return f(x + 10, y) + f(x + 1, y)

    return f(x + 1, y) + f(x + 11, y)

print(f(25, 51))

def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    s = ""
    for c in str(x):
        if c == '9':
            s += c
        else:
            s += str(int(c)+1)

    return f(int(s), y) + f(x+1, y)


print(f(25, 51))