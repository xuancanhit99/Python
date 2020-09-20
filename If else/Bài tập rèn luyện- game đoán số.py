from random import randrange
from time import sleep
print("="*69)
print("Chào mừng bạn đến với game đoán số #cre by: Shinz99")
print("Luật chơi:")
print("1.Máy sẽ tạo ngẫu nhiên số x[1...100]")
print("2.Người chơi đoán số x, chỉ được phép đoán sai 7 lần")
print("3.Mỗi lần đoán sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn\n  số của máy và hiển thị số lần đoán")
print("4.Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần")
print("===================== Chúc bạn chơi game vui vẻ =====================")
while True:
    print("Đang load",end='')
    for x in range(3, 0, -1):
        print(".", end='')
        sleep(1)  # Mỗi 1 giây xuất 1 giá trị
    print()
    x = randrange(1, 101)
    count = 1
    while True:
        print("Lần đoán thứ", count)
        a=int(input("Nhập số mà bạn đoán: "))
        if a>=1 and a<=100:
            if a<x:
                print("Số bạn đoán", a,"< x")
            elif a>x:
                print("Số bạn đoán", a,"> x")
            else:
                break
            if count==7 :
                break
            count+=1
        else:
            print("Bạn vi phạm luật chơi")
            count=7
            break
    if count==7 and x !=a :
        print("===Bạn Thua===")
        print("Số của máy là x =", x)
    else:
        print("===Bạn Thắng===")
    print("Bạn có muốn chơi tiếp hay không(c/k):")
    hoi=input()
    if hoi=='k':
        break
print("Cảm ơn bạn đã chơi game")