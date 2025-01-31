def f(start, end, flag):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 1, end, False) + f(start + 2, end, False) if flag \
            else f(start + 1, end, False) + f(start + 2, end, False) + f(2 * start, end, True)


print(f(1, 9, False))


def f(start, end, km):
    if start == end:
        return 1
    if start > end:
        return 0
    if km == 1:
        return f(start + 1, end, 0) + f(start + 2, end, 0)
    return f(start + 1, end, 0) + f(start + 2, end, 0) + f(start * 2, end, 1)


print(f(1, 9, 0))


"""
Исполнитель преобразует число на экране.
У исполнителя есть три команды, которым присвоены номера:

 Прибавить 1
 Прибавить 2
 Умножить на 2
Первая команда увеличивает число на экране на , вторая увеличивает его на , третья — умножает на .
Программа для исполнителя — это последовательность команд.
Сколько существует программ, которые преобразуют исходное число 1 в число 9,
 и при этом не содержат двух команд умножения подряд?
"""