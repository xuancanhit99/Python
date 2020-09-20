a=int(input("Input a: "))
b=int(input("Input b: "))
pt=input("Input Phep toan:")
if pt == '+':
    print("Kết quả a + b =", a+b)
elif pt == '-':
    print("Kết quả a - b =", a-b)
elif pt == '*':
    print("Kết quả a * b =", a*b)
elif pt == '/':
    print("Kết quả a / b =", a/b)
else:
    print("Bạn nhập không đúng phép toán")
