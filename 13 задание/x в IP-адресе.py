from ipaddress import *
for x in range(256):
    net = ip_network(f'128.0.{x}.5/255.255.240.0', 0)
    for ad in net:
        ad_bin = bin(int(ad))[2:].zfill(32)
        if ad_bin[:16].count('1') > ad_bin[16:].count('1'):
            break
    else:
        print(x)
        break



