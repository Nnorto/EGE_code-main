s = open('24 файл').readline()
s = s.replace('ABB', 'AB AB')
s = s.split(' ')
print(len(max(s, key=len)), s)
