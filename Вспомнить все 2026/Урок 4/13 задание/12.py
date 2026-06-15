from ipaddress import *
net = ip_network('200.229.129.55/255.254.0.0', 0)
cnt = 0
for ad in net:
    ad2 = f'{ad:b}'
    lev = ad2[:len(ad2)//2]
    prav = ad2[len(ad2)//2:]
    if prav.count('1') > lev.count('1') * 2:
        cnt += 1
        
print(cnt)

