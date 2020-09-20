a=0
b=113
if a==0 and b==0:
    print("Vô số nghiệm")
elif a==0 and b!=0:
    print("Vô nghiệm")
else:
    print("Có nghiệm X=", -b/a)



year=2016
if (year % 4==0 and year %100 !=0) or year %400==0:
    print(year," Là năm nhuận")
else:
    print(year, "Không là năm nhuận")
