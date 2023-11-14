n = int(input("Nhap N duong: "))
'''
sum = 0 
for i in range( 1, n+1):
    giaithua = 1
    for j in range(1, i + 1):
        giaithua = giaithua * j
    sum = sum + giaithua
''' 
i = 1
giaithuA=1
s=0
while(i<=n):
    giaithuA = giaithuA * i
    s = s + giaithuA
    i+=1
    
print("F(" + str(n) + ")"  +  " =",s )

