#Nhập vào điểm toán lý hoá bằng chuỗi theo thứ tự:
#Toán,lỹ,hoá-> "7,4,6"
#Tính điểm trung bình lấy 2 chữ số lẻ thập phân.
print("Chương trình tính điểm trung bình")
t,l,h=eval(input("Nhập điểm toán,lý,hoá: "))
tb=(t+l+h)/3
print("Điểm Toán =", t)
print("Điểm Lý =", l)
print("Điểm Hoá =", h)
print("Điểm trung bình =", tb)
print("Điểm làm tròn =", round(tb,2))
