s = open('../file24/24_25dosr.txt').readline()

from string import printable
alf14 = printable[:14].upper()

for x in printable:
    if x not in alf14:
        s = s.replace(x, ' ')
while ' 0' in s:
    s = s.replace(' 0', ' ')
s = s.split()

md = 0
for x in s:
    if len(x) >= md:
        for t in range(len(x)-1, 0, -1):
            ns = x[0:t+1]
            while ns[0] == '0':
                ns = ns[1:]
            if int(ns, 14) % 2 == 0:
                if len(ns) > md:
                    md = len(ns)
                    res = x

                    print(x[:2])

print(res[1])
print(md)


