
x = "0983876207;75;10:18:25;0918295063"
n = x.split(";")
print(n)
s1 = 2500 / 60
print("Mỗi giây cuộc gọi tốn: ",s1)
s2 = s1 * int(n[1])
print("Tổng cuộc gọi tốn: ",s2)