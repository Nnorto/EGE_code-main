def f(x, y):
    if x == y:
        return 1
    """
       if x > y or x == 10: # исключаем из траектории
   """
    if x > y:
        return 0
    return f(x + 1, y) + f(x + 2, y)

print(f(5, 10) * f(10, 15)) # при этом траектория вычислений содержит число 10