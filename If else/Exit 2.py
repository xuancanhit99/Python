while True:
    n=int(input("Nhập một số: "))
    dem=0
    for i in range(1,n+1):
        if n%i == 0:
            dem+=1
    if(dem==2):
        print(n, "Là số nguyên tố")
    else:
        print(n, "Không là số nguyên tố")
    print("Tiếp hay không(c/k): ")
    if input()=='k':
        break
print("Bye")