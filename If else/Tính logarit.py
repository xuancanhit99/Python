#Viết chương trình tính log-a-(x) với a,x là các số nhập vào từ bàn phím
# x>0,a>0,a!=1(a khác 1)
#dùng hàm log-a-(x)=lnx/lna)
from math import log

print("Chương trình tính loga cơ số a của x")
a=float(input("Nhập vào a = "))
x=float(input("Nhập vào x = "))
if a>0 and a!=1 and x>0:
    l=log(x)/log(a)
else:
    print("Vi phạm điều kiện tồn tại logarit")
print("log-a-(b) =", l)