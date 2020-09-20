print("-----Tính phần trăm phiếu bầu-----")
m=int(input("Nhập số lượng các ứng cử viên: "))
n=int(input("Nhập số lượng cần bầu: "))
s1=int(input("Nhập số lượng cử tri trong danh sách: "))
s2=int(input("Nhập số lượng cử tri đi bỏ phiếu: "))
s3=int(input("Nhập số lượng số phiếu bầu hợp lệ"))
sa= round(((s2/s1)*100),2) #Phần trăm số lượng cử tri đi bỏ phiếu
print("Các ứng cử viên sẽ được sắp xếp theo số thứ tự từ 1 đến", n)
i=0
while m>0 and i<m:
    i+=1
    a=int(input("Nhập số phiếu ứng cử viên", i,":" )
    pt1=(a/s2)*100
    pt=round(pt1,2)
    print('Ứng cử viên 1 được {0} phiếu bầu({1}/{2} phiếu bị gạch), đạt {3} %'.format(a,s2-a,s2,pt))
    m-=1

