from random import randrange
count=0
while True:
    x=randrange(-100,100)
    count+=1
    print(x, end=',')
    if x==50:
        break
    print("Đếm =", count)
print("Ok")