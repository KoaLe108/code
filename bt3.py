n = str(input("Nhập chuỗi N : "))
y = str(input("Nhập chuỗi Y: "))
chuoi1 = 0
chuoi2 = 0
for i in n:
    chuoi1 += 1
print("Số kí tự chuỗi 1: ", chuoi1)
for i in y:
    chuoi2 += 1
print("Số kí tự chuỗi 2: ", chuoi2)
if chuoi1 > chuoi2:
    print("Chuỗi 1 dài 2 chuỗi 2")
elif chuoi1 < chuoi2:
    print("Chuỗi 1 ngắn hơi chuỗi 2")
else:
    print("2 chuỗi dài bằng nhau")
