from ipaddress import *
k = 0
net = ip_network('106.184.0.0/255.248.0.0')
for ad in net:
    ad = list(map(int, str(ad).split('.')))
    ad2 = ''
    for i in range(4):
        ad2 += bin(ad[i])[2:].zfill(8)
    if ad2.count('1') % 2 != 0:
        k += 1
print(k)


k = 0
net = ip_network('106.184.0.0/255.248.0.0')
for ad in net:
    dv = bin(int(ad))[2:].zfill(32)
    if dv.count('1') % 2 == 1:
        k += 1

print(k)

k = 0
net = ip_network('106.184.0.0/255.248.0.0')
for ad in net:
    dv = f'{ad:b}'
    if dv.count('1') % 2 == 1:
        k += 1

print(k)