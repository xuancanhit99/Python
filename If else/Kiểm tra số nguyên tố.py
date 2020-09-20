print("Chương trình kiểm tra số nguyên tố")
while True:
    x=int(input("Nhập số kiểm tra: "))
    nt=1
    for i in range(2,x):
        if (x%i==0):
            nt=0
            break
    if (nt):
        print(x, "Là số nguyên tố")
    else:
        print(x, "Không là số nguyên tố")
    h=input("Tiếp tục chương trình hay không(c/k): ")
    if h=='k':
        break
print("Đã thoát phần mềm")
