n=int(input("Nhập số * cạnh của hình vuông: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end='')
        else:
            print(" ",end='')
    print()
print("-"*20)
m=int(input("Nhập số * cạnh bên của tam giác vuông cân: "))
for i in range(1,m+1):
    for j in range(1,m+1):
        if j==m or i==m or i+j==m+1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
print("-"*20)
x=int(input("Nhập số * dòng: "))
for i in range(1,x+1):
    for j in range(1,x+1):
        if i==j or i==x/2 or (j==1 and i<x/2) or (j==x and i>x/2):
            print("*",end='')
        else:
            print(" ",end='')
    print()

