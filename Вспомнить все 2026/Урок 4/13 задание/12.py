from ipaddress import *
net = ip_network('56.141.128.222/255.255.252.0', 0)
cnt = 0
for ad in net:
    ad2 = f'{ad:b}'
    lev = ad2[:len(ad2)//2]
    prav = ad2[len(ad2)//2:]
    if prav.count('0') % 2 == 0:
        if lev.count('1') <= prav.count('0'):
            cnt += 1

print(cnt)

