from time import clock

start=clock()
print("Mời bạn nhập một giá trị")
x=input()
print("Bạn nhập x=", x)
end=clock()
duration=end-start
print("Thời gian nhập: ", duration)
start=clock()
for x in range(100000):
    print(x,end='')
end=clock()
duration=end-start
print("Thời gian chạy: ", duration)