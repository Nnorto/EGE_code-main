from ipaddress import *
for A in range(16, 25):
    net = ip_network(f'117.157.2.8/{A}', 0)
    flag = True
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') < ad_bin[16:].count('1'):
            flag = False
            break
    if flag:
        print(A)

print('или')

for A in range(9):
    net = ip_network(f'117.157.2.8/{16+A}', 0)
    flag = True
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') < ad_bin[16:].count('1'):
            flag = False
            break
    if flag:
        print(A)