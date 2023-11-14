def kiemtra(a,b,c):
    if (a-b == b-c):
        return False
    else: return True;
a, b, c = int(input("A = ")), int(input("B = ")), int(input("C = "))

if kiemtra(a,b,c) or kiemtra(a,c,b) or kiemtra(b,a,c) or kiemtra(b,c,a) or kiemtra(c,a,b) or kiemtra(c,b,a):
    print("Nhiem vu hoan thanh")
else: print("Nhiem vu that bai")