f = open('Файлы/СборникЕГЭ_2024_задание24_3.txt')
s = f.readline()
print(len(s))
for x in '123456789':
    s = s.replace(x, '1')
s = s.replace('+*', ' ')
s = s.replace('++', ' ')
s = s.replace('*+', ' ')
s = s.replace('**', ' ')
while ' *' in s:
    s = s.replace(' *', ' ')
while '* ' in s:
    s = s.replace('* ', ' ')
while '+ ' in s:
    s = s.replace('+ ', ' ')
while ' +' in s:
    s = s.replace(' +', ' ')
s = s.replace('+01', '+0 1')
s = s.replace('*01', '*0 1')
maxd = 0
s = s.split()
#ln = len(s)
for t in range(len(s)):
    x = s[t]
    if len(x) > maxd:
        for i in range(len(x) - 1):
            if x[i] not in ['+', '*'] and x[i] + x[i+1] not in ['00', '01']:
                ns = x[i]
                for j in range(i+1, len(x)):
                    ns += x[j]
                    if len(ns) > maxd:
                        if ns[-1] not in ['+', '*']:
                            if eval(ns) == 0:
                                maxd = max(maxd, len(ns))
    # pg = (t*100)/ln
    # if int(pg) % 10 == 0 and int(pg) == pg:
    #     print(pg, maxd)
print(maxd)