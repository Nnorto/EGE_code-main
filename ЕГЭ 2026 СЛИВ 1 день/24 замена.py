s = open('ЕГЭ 2026 день 1.txt').readline()
s = s.replace('*', '+')
for x in '123456789':
    s = s.replace(x, '1')
while '++' in s:
    s = s.replace('++', '+ +')
s = s.replace(' +', ' ')
s = s.replace('+ ', ' ')
while '+00' in s:
    s = s.replace('+00', '+0 0')
while '+01' in s:
    s = s.replace('+01', '+0 1')
s = s.split()
print(len(max(s, key=len)))

#Если произведение равно нулю

s = open('ЕГЭ 2026 день 1.txt').readline()
for x in '123456789':
    s = s.replace(x, '1')
while '**' in s or '++' in s or '+*' in s or '*+' in s:
    s = s.replace('**', '* *')
    s = s.replace('++', '+ +')
    s = s.replace('+*', '+ *')
    s = s.replace('*+', '* +')
while '+ ' in s or ' +' in s:
    s = s.replace(' +', ' ')
    s = s.replace('+ ', ' ')
while '* ' in s or ' *' in s:
    s = s.replace(' *', ' ')
    s = s.replace('* ', ' ')
s = s.split()
md = 0
for x in s:
    if len(x) > md:
        ns = ''
        for t in range(len(x)):
            ns += x[t]
            try:
                if eval(ns) == 0 and len(ns) > md:
                    md = len(ns)
            except:
                pass

print(md)
