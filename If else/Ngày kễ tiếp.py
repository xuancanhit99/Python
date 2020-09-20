print("Program Next Day")
d=int(input("Input Day: "))
m=int(input("Input Month: "))
y=int(input("Input Year: "))
if y>0:
    if m==12:
        if d in range(1,31):
            d += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        elif d==31:
            d = 1
            m = 1
            y += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        else:
            print("Input Wrong")
    elif m in (4, 6, 9, 11):
        if d in range(1,30):
            d += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        elif d == 30:
            d = 1
            m += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        else:
            print("Input Wrong")
    elif m == 2:
        if d in range(1,28):
            d += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        elif d in (28, 29):
            if d==28:
                if (y % 4 == 0 and y % 100 != 0) or y%400==0:
                    d += 1
                else:
                    d = 1
                    m += 1
                print('Next Day: {0}-{1}-{2}'.format(d, m, y))
            else:
                if (y % 4 == 0 and y % 100 != 0) or y%400==0:
                    d = 1
                    m += 1
                    print('Next Day: {0}-{1}-{2}'.format(d, m, y))
                else:
                    print("Input Wrong")
        else:
            print("Input Wrong")
    elif m in (1, 3, 5, 7, 8, 10):
        if d in range(1,31):
            d += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        elif d == 31:
            d = 1
            m += 1
            print('Next Day: {0}-{1}-{2}'.format(d, m, y))
        else:
            print("Input Wrong")
    else:
        print("Input Wrong")
else:
    print("Input Wrong")
