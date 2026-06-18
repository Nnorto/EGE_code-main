s = open('СборникЕГЭ_2024_задание24_3.txt').readline()
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
