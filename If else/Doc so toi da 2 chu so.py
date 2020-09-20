print("Chương trình đọc số có tối đa 2 chữ số")
x=int(input("Nhập số: "))
m="Mốt"
m1="Một"
h2="Hai"
b3="Ba"
b4="Bốn"
n5="Năm"
s6="Sáu"
b7="Bảy"
t8="Tám"
c9="Chín"
m10="Mười"
m0="Mươi"
if x>=0 and x<=10:
    if x==1:
        print(m1)
    elif x==2:
        print(h2)
    elif x==3:
        print(b3)
    elif x==4:
        print(b4)
    elif x==5:
        print(n5)
    elif x==6:
        print(s6)
    elif x==7:
        print(b7)
    elif x==8:
        print(t8)
    elif x==9:
        print(c9)
    elif x==10:
        print(m10)
    else:
        print("Không")
elif x > 10 and x < 20:
    y=x-10
    if y==1:
        print(m10, m1)
    elif y==2:
        print(m10, h2)
    elif y==3:
        print(m10, b3)
    elif y==4:
        print(m10, b4)
    elif y==5:
        print(m10, n5)
    elif y==6:
        print(m10, s6)
    elif y==7:
        print(m10, b7)
    elif y==8:
        print(m10, t8)
    elif y==9:
        print(m10, c9)
elif x in (20,30,40,50,60,70,80,90):
    y=x/10

elif x in (21,31,41,51,61,71,81,91):
    y=(x-1)/10
    if y==2:
        print(h2, m0, m)
    elif y==3:
        print(b3, m0, m)
    elif y==4:
        print(b4, m0, m)
    elif y==5:
        print(n5, m0, m)
    elif y==6:
        print(s6, m0, m)
    elif y==7:
        print(b7, m0, m)
    elif y==8:
        print(t8, m0, m)
    elif y==9:
        print(c9, m0, m)
elif x in (22,32,42,52,62,72,82,92):
    y=(x-2)/10
    if y==2:
        print(h2, m0, h2)
    elif y==3:
        print(b3, m0, h2)
    elif y==4:
        print(b4, m0, h2)
    elif y==5:
        print(n5, m0, h2)
    elif y==6:
        print(s6, m0, h2)
    elif y==7:
        print(b7, m0, h2)
    elif y==8:
        print(t8, m0, h2)
    elif y==9:
        print(c9, m0, h2)
elif x in (23,33,43,53,63,73,83,93):
    y=(x-3)/10
    if y==2:
        print(h2, m0, b3)
    elif y==3:
        print(b3, m0, b3)
    elif y==4:
        print(b4, m0, b3)
    elif y==5:
        print(n5, m0, b3)
    elif y==6:
        print(s6, m0, b3)
    elif y==7:
        print(b7, m0, b3)
    elif y==8:
        print(t8, m0, b3)
    elif y==9:
        print(c9, m0, b3)




