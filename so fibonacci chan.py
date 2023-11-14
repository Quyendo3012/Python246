def isFibo(a,b,n):
    if n==b or n==0:
        return 1
    if n<b:
        return 0
    return isFibo(b,a+b,n)

n = int(input("N = "))
if isFibo(0,1,n)==1:
    if n%2==0:
        print("N la so fibonacci chan")
    else:
        print("N khong phai la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")
