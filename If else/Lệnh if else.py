a=int(input("Input a: "))
s=0
for i in range(5,10):
    if a%2!=0:
        print("Stop")
        break
    s+=i
else:
    print("Sum=", s)