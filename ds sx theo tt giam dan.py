n = int(input("Nhap N: "))
n1 = int(input("Nhap gia tri thu 1: "))
n2 = float(input("Nhap gia tri thu 2: "))
n3 = int(input("Nhap gia tri thu 3: "))
n4 = str(input("Nhap gia tri thu 4: "))
n5 = float(input("Nhap gia tri thu 5: "))
l = [n1,n2, n3, n4, n5]
a = sorted ( l, key = int, reverse = False )
b = sorted ( l, key = float, reverse = False )
c = sorted ( l, key = str, reverse = False )

print("A = ", a)
print("B = ", b)
print("C = ",c)
