for i in range(258274,258297+1):
    kd=0
    mas= []
    for d in range(2, i):
        if i % d == 0:
            kd+=1
            mas.append(d)
    if kd==2:
        print(mas)