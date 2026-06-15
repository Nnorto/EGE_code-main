f = open('26 банкоматы.txt')
cnt_bank, cnt_client = [int(x) for x in f.readline().split()]
day = 24*60
last_bank = 0
bank = [0] * cnt_bank
clients = []
cnt = 0
for s in f:
    time, obsl = [int(x) for x in s.split()]
    clients.append([time, obsl])

clients.sort()
for time, obsl in clients:
    id_min_bank = bank.index(min(bank))
    if bank[id_min_bank] <= day:
        if bank[id_min_bank] >= time:
            bank[id_min_bank] += obsl
            cnt += 1
            last_bank = id_min_bank + 1
        else:
            bank[id_min_bank] += time + obsl
            cnt += 1
            last_bank = id_min_bank + 1

print(cnt, last_bank)