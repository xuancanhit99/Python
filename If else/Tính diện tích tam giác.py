#Nhập vào 3 cạnh của một tam giác. Kiểm tra tính hợp lệ
#Sau đó tính diện tích theo công thức Herong
from math import sqrt

print("Tính diện tích tam giác")
print("Nhập số đo 3 cạnh của một tam giác")
a=float(input("Nhập số đo cạnh thứ nhất a = "))
b=float(input("Nhập số đo cạnh thứ hai b = "))
c=float(input("Nhập số đo cạnh thứ ba c = "))
#S=0
p=(a+b+c)/2
# S=round(sqrt(p*(p-a)*(p-b)*(p-c)),2) Bỏ vào trong hàm if để kiểm tra trước, tránh lỗi căn bậc 2 của một số âm
# Lỗi ValueError: math domain error - Miền toán học
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    S = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    if a==b and a==c:
        S1=pow(a,2)*(sqrt(3)/4)
        print("Đây là tam giác đều")
        print("Diện tích tam giác là S =", round(S1,2))
    elif (a==b or b==c or a==c) and (pow(a,2)==pow(b,2)+pow(c,2) or pow(b,2)==pow(a,2)+pow(c,2) or pow(c,2)==pow(a,2)+pow(b,2)):
        print("Đây là tam giác vuông cân")
        if pow(a,2)==pow(b,2)+pow(c,2):
            S1=(1/2)*b*c
        elif pow(b,2)==pow(a,2)+pow(c,2):
            S1=(1/2)*a*c
        else:
            S1=(1/2)*a*b
        print("Diên tích tam giác là S =", round(S1,2))
    elif a==b or b==c or a==c:
        print("Đây là tam giác cân")
        if a==b:
            h=sqrt(pow(a,2)-pow(c/2,2))
            S1=(1/2)*h*c
        elif b==c:
            h=sqrt(pow(b,2)-pow(a/2,2))
            S1=(1/2)*h*a
        else:
            h=sqrt(pow(a,2)-pow(b/2,2))
            S1=(1/2)*h*b
        print("Diện tích tam giác là S =", round(S1,2))
    elif pow(a,2)==pow(b,2)+pow(c,2) or pow(b,2)==pow(a,2)+pow(c,2) or pow(c,2)==pow(a,2)+pow(b,2):
        print("Đây là tam giác vuông")
        if pow(a,2)==pow(b,2)+pow(c,2):
            S1=(1/2)*b*c
        elif pow(b,2)==pow(a,2)+pow(c,2):
            S1=(1/2)*a*c
        else:
            S1=(1/2)*a*b
        print("Diên tích tam giác là S =", round(S1,2))
    else:
        print("Đây là tam giác thường")
        print("Diện tích tam giác là S =", S)
else:
    print("Không phải tam giác!")
