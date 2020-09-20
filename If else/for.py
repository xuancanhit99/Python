n=int(input("Nhập n:"))
s=0
if n % 2 == 0:
    for x in range(2,n+1,2):
        s+=x
elif n % 2 != 0:
    for x in range(1,n+1,2):
        s+=x
print("Tống S=", s)