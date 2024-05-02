from itertools import *
alf="ГИПЕРБОЛА"
index=0
count=0
for x in product(alf,repeat=6):
    s = "".join(x)
    index+=1
    s=s.replace("И","1")
    s=s.replace("Е","1")
    s=s.replace("О","1")
    s=s.replace("А","1")
    s=s.replace("Г","2")
    s=s.replace("П","2")
    s=s.replace("Р","2")
    s=s.replace("Б","2")
    s=s.replace("Л","2")
    if s[0]!="1" and s[-1]!="1":
        if "212" not in s:
            count+=1
print(count)