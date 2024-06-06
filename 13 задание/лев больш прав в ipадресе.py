from ipaddress import *
k = 0
net = ip_network('157.180.63.114/255.255.255.248', 0)
for ad in net:
    dv = bin(int(ad))[2:].zfill(32)
    lev = dv[:len(dv)//2].count('1')
    prav = dv[len(dv)//2:].count('1')
    if lev < prav:
        k += 1

    # print(lev, prav)
    # print(dv[:len(dv)//2], dv[len(dv)//2:])
    # print(len(dv[:len(dv)//2]), len(dv[len(dv)//2:]))
    # input()

print(k)

