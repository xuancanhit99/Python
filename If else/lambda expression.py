def handle(f,x):
    return f(x)
kq1=handle(lambda x:x**2,9)
print("kq1 =", kq1)
kq2=handle(lambda x:x%2==0,4)
print("kq2 =", kq2)

def LaSoChan(x):
    return x%2==0
kq3=handle(LaSoChan, 4)
print("kq3 =", kq3)
kq4=handle(LaSoChan, 5)
print("kq4 =", kq4)
kq5=handle(lambda x:LaSoChan(x),7)
print("kq5 =", kq5)
