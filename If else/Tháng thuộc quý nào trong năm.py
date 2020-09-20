a=int(input("Input month: "))
if a in (1,2,3):
    print(a, "Thuộc quý 1")
elif a in (4,5,6):
    print(a, "Thuộc quý 2")
elif a in (7,8,9):
    print(a, "Thuộc quý 3")
elif a in (10,11,12):
    print(a, "Thuộc quý 4")
else:
    print("Bạn nhập tháng không đúng")