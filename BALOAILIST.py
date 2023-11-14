n = int(input("Nhap N: "))
D = []
A = []
B = []
C = []
for i in range(n):
    D.append(input("Nhap gia tri thu "+str(i+1)+": "))
for i in D:
    if i.isdigit() or ("-" in i and "." not in i):
        A.append(int(i))
    elif "." in i:
        B.append(float(i))
    elif i.startswith("."):
        i.insert(0, "0")
        B.append(float(i))
    elif i.isalpha():
        C.append(i)
    else:
        C.append(i)
A = set(A)
B = set(B)
C = set(C)
print("A =", sorted(list(A), reverse=True))
print("B =", sorted(list(B), reverse=True))
print("C =", sorted(list(C), reverse=True))