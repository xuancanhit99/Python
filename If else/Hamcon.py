def PTB1(a,b):
    """Đây là hàm
    giải phương trình bậc 2"""
    if a==0 and b==0:
        return "Vô số nghiệm"
    elif a==0 and b!=0:
        return "Vô nghiệm"
    else:
        return "x={0}".format(-b/a)
def XuatDuLieu(data):
    """Hàm xuất dữ liệu"""
    print(data)


kq=PTB1(0,0)
kq2=PTB1(0,1)
kq3=PTB1(6,7)
print(kq)
print(kq2)
print(kq3)

kq4=PTB1(3,7)3
XuatDuLieu(kq4)
