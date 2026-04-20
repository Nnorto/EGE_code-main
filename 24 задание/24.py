s = open('Файлы/24-j6.txt').read()
k = 0
if s[-7] < s[-6] < s[-5] < s[-4] < s[-3] < s[-2]< s[-1]:
    k += 1

for i in range(7, len(s)):
    if s[i-7] < s[i-6] < s[i-5] < s[-4] < s[i-3] < s[i-2]< s[i-1] and s[i-1] > s[i]:
        k+=1
print(k)