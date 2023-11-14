#import math
N = int(input("N = "))

a, sum = 0, 0
for i in range(1, N+1):
    a = a + i
    sum = sum + pow(a, 1/i)
print("F(" + str(N) + ") =", '{:.7f}'.format(sum))
