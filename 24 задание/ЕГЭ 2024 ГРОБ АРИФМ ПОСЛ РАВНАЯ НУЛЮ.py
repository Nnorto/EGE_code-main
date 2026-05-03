s = open('Файлы/СборникЕГЭ_2024_задание24_3.txt').readline()

for x in '123456789':
    s = s.replace(x, '1')

while '++' in s or '**' in s or '+*' in s or '*+' in s:
    s = s.replace('++', '+ +')
    s = s.replace('**', '* *')
    s = s.replace('*+', '* +')
    s = s.replace('+*', '+ *')

while '+ ' in s or '* ' in s:
    s = s.replace('+ ', ' ')
    s = s.replace('* ', ' ')

while ' +' in s or ' *' in s:
    s = s.replace(' +', ' ')
    s = s.replace(' *', ' ')

while ' 00' in s:
    s = s.replace(' 00', ' 0 0')
while ' 01' in s:
    s = s.replace(' 01', ' 0 1')
while '+01' in s:
    s = s.replace('+01', '+0 1')
while '*01' in s:
    s = s.replace('*01', '*0 1')


s = s.split()
ln = len(s)

md = 0
cnt = 0
for x in s:
    cnt +=1
    if len(x) > md:
        for i in range(len(x) - 1):
            if x[i] not in '*+' and x[i] + x[i+1] != '01' and x[i] + x[i+1] != '00':
                ns = x[i]
                for j in range(i + 1, len(x)):
                    ns += x[j]
                    if x[j] not in '*+':
                       if eval(ns) == 0 and len(ns) > md:
                            md = max(md, len(ns))
    print(md, cnt/ln*100)
print(md)