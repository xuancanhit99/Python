from math import sqrt
print("Giải phương trình bậc 2: ax^2 + bx +c = 0")
a=float(input("Mời bạn nhập a: "))
b=float(input("Mời bạn nhập b: "))
c=float(input("Mời bạn nhập c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm duy nhất ")
        print("x =", -c/b)
else:
    d=b*b - 4*a*c
    if d>0:
        x1=(-b + sqrt(d))/(2*a)
        x2=(-b - sqrt(d))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 =", x1)
        print("x2 =", x2)
    elif d<0:
        print("Phương trình vô nghiệm")
    else:
        x=-b/(2*a)
        print("Phương trình có nghiệm kép")
        print("x =", x)