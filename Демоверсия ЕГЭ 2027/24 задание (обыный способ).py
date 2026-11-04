s = open('demo_24.txt').readline()
s = ' ' + s + ' '
s = s.replace('6', '1')
s = s.replace('7', '1')
s = s.replace('8', '1')
s = s.replace('9', '1')
s = s.replace('-', '*')
s = s.replace(' 0', ' ')
s = s.replace('* ', ' ')
s = s.replace('- ', ' ')
while '**' in s:
    s = s.replace('**', '* *')
while '*00' in s:
    s = s.replace('*00', '*0 0')
while ' 00' in s:
    s = s.replace(' 00', ' 0 0')
while '1* ' in s:
    s = s.replace('1* ', '1 ')
while ' *' in s:
    s = s.replace(' *', ' ')
while '* ' in s:
    s = s.replace('* ', ' ')
res = []
for x in s.split():
    res.append(len(x))
print(max(res))