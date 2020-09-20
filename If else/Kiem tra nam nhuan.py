print("Chương trình kiểm tra năm nhuần")
year=int(input("Nhập năm cần kiểm tra: "))
#print("Năm nhuần" if (year%4==0 and year%100!=0) or year%400==0) else "Năm không nhuần")
if (year%4==0 and year%100!=0) or year%400==0:
    print('Năm {0} là năm nhuần'.format(year))
else:
    print("Năm", year, "không phải là năm nhuần")