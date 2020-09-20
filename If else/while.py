a=1
while a>0:
    if a<9:
        print("Lặp liên tục")
    else:
        break
    a+=1
print(a)


value=-1
while value < 1 or value > 10:
    value=int(input("Nhập giá trị [1..10]:"))
print("value=", pow(value,2))