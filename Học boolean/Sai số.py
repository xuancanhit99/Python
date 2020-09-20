d1=1.11-1.10
d2=2.11-2.10
print("d1=", d1, "d2=", d2)
saiso=d1-d2
if saiso < 0:
    saiso = -saiso
if saiso < 0.000001 :
    print("Same")
else:
    print("Dif")