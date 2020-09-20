def BMI(h,m):
    return m/(h**2)
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi >= 18.5 and bmi < 25:
        return "Bình thường"
    elif bmi >= 25 and bmi < 30:
        return "Hơi béo"
    elif bmi >= 30 and bmi < 35:
        return "Béo phì cấp độ 1"
    elif bmi >= 35 and bmi <= 40:
        return "Béo phì cấp độ 2"
    elif bmi > 40:
        return "Béo phì cấp độ 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi >= 18.5 and bmi < 25:
        return "Trung bình"
    elif bmi >= 25 and bmi < 30:
        return "Cao"
    elif bmi >= 30 and bmi < 35:
        return "Cao"
    elif bmi >= 35 and bmi <= 40:
        return "BRất cao"
    elif bmi > 40:
        return "Nguy hiểm"
print("===Chào mừng bạn đến với chương trình tính BMI===")
while True:
    h1 = int(input("Nhập vào chiều cao của bạn(cm): "))
    m = int(input("Nhập vào cân nặng của bạn(kg): "))
    h = h1 / 100
    if h > 0 and m > 0:
        bmi=BMI(h,m)
        print("Chỉ số BMI của bạn = ", round(bmi,2))
        print("Phân loại bạn:", PhanLoai(bmi))
        print("Nguy cơ bệnh của bạn:", NguyCoBenh(bmi))
    else:
        print("Bạn nhập không đúng")
    hoi = input("Bạn có muốn kiểm tra tiếp (c/k)?")
    if hoi == 'k':
        break
print("Cảm ơn bạn đã dùng chương trình")

