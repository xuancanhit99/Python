n=int(input("Nhập N="))
s=0
for x in range(1,n+1):
    s+=x
    if s>=15:
        break
print("S=",s)