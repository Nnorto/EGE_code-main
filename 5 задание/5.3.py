for n in range(2, 1000):
     n2 = bin(n)[2::]
     n2 += n2[-2]
     n2 += n2[1]
     r = int(n2, 2)
     if r > 170:
         print(n)
         break