def ROI(DT,CP):
    return (DT-CP)/CP
def TuVan(rol):
    if rol < 0.75:
        return "Không nên đầu tư"
    else:
        return "Nên đầu tư"

print("Chương trình tư vấn có nên đầu tư hay không")
while True:
    dt=int(input("Nhập vào doanh thu: "))
    cp=int(input("Nhập vào chi phí: "))
    rol=ROI(dt,cp)
    print("Tỉ lệ rol = ", round(rol,2))
    TuVan(rol)
    print("Lời khuyên:", TuVan(rol))
    print("Tiếp tục tư vấn(c/k)")
    if input() == 'k':
        break
print("Cảm ơn bạn đã dùng chương trình")
