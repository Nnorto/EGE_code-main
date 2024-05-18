f = open("24 (1).txt")

s = f.read()
def isChar(c):
    if c == 'A':
        return True
    elif c == 'B':
        return True
    elif c == 'C':
        return True
    return False

def isNum(c):
    if c == '6':
        return True
    elif c == '7':
        return True
    elif c == '8':
        return True
    elif c == '9':
        return True
    return False
maxCounter = 0
locCounter = 1
for i in range(len(s)-1):
    now = s[i]
    next = s[i+1]
    if isChar(now) and isChar(next):
        if locCounter > maxCounter:
            maxCounter = locCounter
        locCounter = 1
    elif isNum(now) and isNum(next):
        if locCounter > maxCounter:
            maxCounter = locCounter
        locCounter = 1
    else:
        locCounter += 1

print(maxCounter)