print("Số ngày trong tháng")
m=int(input("Nhập vào tháng cần kiểm tra: "))
if m in (1,3,5,7,8,10,12):
    print("Tháng", m, "Có 31 ngày")
elif m==2:
    y=int(input("Vui lòng nhập thêm năm: "))
    if (y%4==0 and y%100!=0) or y%400==0:
        print("Tháng", m, "Có 29 ngày")
    else:
        print("Tháng", m, "Có 28 ngày")
elif m in (4,6,9,11):
    print("Tháng", m, "Có 30 ngày")
else:
    print("Bạn nhập tháng không hợp lệ")