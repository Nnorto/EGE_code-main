import re
from fnmatch import *
for n in range(0, 10**10, 2024):
    s = str(n)
    if fnmatch(s, '3?2758*4'):
        print(n, n // 2024)

print("     =    ")

for n in range(0, 10**10, 2024):
    if re.fullmatch(r'3\d2758\d*4', str(n)):
        print(n, n // 2024)