from time import sleep

a=int(input("Nhập a="))
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==(a+1)/2 or (j==(a+1)/2 and i<=(a+1)/2) or (j==1 and i>=(a+1)/2) \
                or (i+j==a+1 and i>=(a+1)/2) or (i<=(a+1)/2 and (j+1)-i==(a+1)/2):
            print("*",end='')
            sleep(0.1)
        else:
            print(" ",end='')
            sleep(0.1)
    print()
print("="*30)
b=int(input("Nhập b="))
for i in range(1,b+1):
    for j in range(1,b+1):
        if j==(b+1)/2 or i+j==b+1 or (i==1 and j>=(b+1)/2) or (i==b and j<=(b+1)/2):
            print("*",end='')
            sleep(0.1)
        else:
            print(" ",end='')
            sleep(0.1)
    print()
