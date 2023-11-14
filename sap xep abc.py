a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
m = max(a, b, c)
if a == m:
    a, b, c = min(b,c), max(b,c), a
elif b == m:
    a, b, c = min(a,c), max(a,c), b
elif c == m:
    a, b, c = min(a,b), max(a,b), c
if a == c: print("Xep tang dan:", a)
elif a == b: print("Xep tang dan:", a,c)
elif b == c: print("Xep tang dan:", a,b)
else: print("Xep tang dan:", a, b, c)

