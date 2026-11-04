f = open('demo_26.txt')
ogr_h = 11
ogr_m = 59
ogr_s = 59
n, server = [int(x) for x in f.readline().split()]
data = []
for s in f:
    s = s.split()
    hour, min, sec = [int(x) for x in s[0].split(':')]
    client = int(s[1])
    v = int(s[2])
    data.append([hour, min, sec, client, v])

clients = []
data_clients = []
ost = server
data_rezerv = []
for hour, min, sec, client, v in data:
    if ost - v >= 0:
        ost -= v
        if client not in clients:
            clients.append(client)
            data_clients.append(v)
        else:
            ind = clients.index(client)
            data_clients[ind] += v
    else:
        if hour <= ogr_h and min <= ogr_m and sec <= ogr_s:
            rez = server - ost
            data_rezerv.append(rez)
            ost = server
            ost -= v
        if client not in clients:
            clients.append(client)
            data_clients.append(v)
        else:
            ind = clients.index(client)
            data_clients[ind] += v


ind = data_clients.index(max(data_clients))
data_rezerv.sort()
print(clients[ind], data_rezerv[-1]+data_rezerv[-2])
