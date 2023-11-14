from math import sqrt


n = int(input("N = "))
sum = 0 

for i in range(1, n+1):
    sum = sqrt(i + sum)
    i = i + 1
    
print("F(" + str(n) + ")"  +  " =", sum+1 )
    