for n in range(5, 100):
    for k in range(5, 100):
        s = "2" * k + "5" * n

        while "25" in s or "355" in s or "555" in s:
            if "25" in s:
                s = s.replace("25", "5", 1)
            if "355" in s:
                s = s.replace("355", "52", 1)
            if "555" in s:
                s = s.replace("555", "3", 1)

        """if s.count("2") > 0 and s.count("5") > 0 and s.count("3") > 0 and s.count("2") % 2 == 0:
            print(n, k, s, n+k, "<= ответ")"""

        if ('2' in s) and ("3" in s) and ("5" in s) and s.count("2") % 2 == 0:
            print(n, k, "|| >>>", n+k, "<<< ответ")