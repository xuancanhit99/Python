while True:
    x=int(input("Nhập vào x="))
    print(x, "Là số chẵn" if x % 2 == 0 else "Là số lẻ")
    hoi=input("Tiếp hay không (c/k):")
    if hoi=='k':
        break
print("Bye")