from ipaddress import *

net = ip_network('124.8.0.0/255.248.0.0', 0)

max_zero = 0
for ad in net:
    if ad != net.network_address and ad != net.broadcast_address:
        ad_bin = bin(int(ad))[2:].zfill(32)
        max_zero = max(max_zero, ad_bin.count('0'))
print(max_zero)


# Сеть дается ір- адресами.
# Самый маленький ір-адрес, - это адрес сети,
# в нем все нули на тех местах, где маски можно менять,
# а самый большой ір-адрес,
# где наоборот единицы - это широковещательный.
# По хорошему в условии должно быть написано,
# что широковещательный и адрес сети не учитываются.
# (иначе максимальное количество нулей содержится в адресе сети )
# Чтобы такое учесть мы пишем такую строчку:
# if ad =! net.network_address and ad =! net.broadcast_address