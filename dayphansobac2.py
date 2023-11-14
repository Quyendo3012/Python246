N = int(input("N = "))
s, F= 0, 0 
for i in range(1, N+1):
    s = s + i**2
    F = F + N / s
print("F(" + str(N) + ") =", '{:.7f}' .format(F))
   