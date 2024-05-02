def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return f(start + 1, end) + f(start + 11, end)


print(f(25, 51))