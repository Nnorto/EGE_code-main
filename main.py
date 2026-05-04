from ipaddress import *

for mask in range(16, 24+1):
    net = ip_network(f'255.211.33.160/{mask}', False)
    flag = True
    for ad in net:
        ad2 = f'{ad:b}'
        lev = ad2[:16]
        prav = ad2[16:]
        if not(lev.count('1') >= prav.count('1')):
            flag = False
            break
    if flag:
        print(net.netmask)
        break