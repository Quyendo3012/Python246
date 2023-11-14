a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a: 
    print("Khong phai tam giac")
else:
    print("Dung la tam giac")
     