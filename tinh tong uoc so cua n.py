
n = int(input("N = "))
sum = 0
for i in range(1,n+1):
    if (n%i ==0):
        sum+=i  
print("Tong cac uoc so cua",n,"la",sum)
