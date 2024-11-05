t_c1 = int(input())
t_m1 = int(input())
t_s1 = int(input())
t_c2 = int(input())
t_m2 = int(input())
t_s2 = int(input())
k = (t_c1*3600) + t_m1 * 60 + t_s1
r = (t_c2*3600) + t_m2 * 60 + t_s2
print(r - k)