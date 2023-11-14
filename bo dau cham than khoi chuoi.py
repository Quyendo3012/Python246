org_str = input("Nhap S: ")
if org_str('!') == 1:
    new_str = org_str.rstrip("!")
    print("Chuoi S sau khi loai bo dau cham than:",new_str)
elif org_str('!!!') ==1: 
    new_str = org_str.rstrip("!!!")
    print("Chuoi S sau khi loai bo dau cham than:",new_str)
else:
    new_str = org_str
    print("Chuoi S sau khi loai bo dau cham than:",new_str)
