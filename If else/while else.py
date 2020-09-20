print("Chương trình tính trung bình cộng 5 số dương")
print("Nhập danh sách cac số dương để tính TBC")
count = s = 0
while count < 5:
    val = float(input("Nhập số: "))
    if val < 0:
        print("Số sai quy tắc, thoát")
        break # gặp lệnh break nhảy khỏi while và else
    count += 1
    s += val
else: # Thực hiện while xong nhảy qua else
    print("Trung Bình =", s/count)