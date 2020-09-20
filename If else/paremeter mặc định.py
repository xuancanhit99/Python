def FN(n,m=0):
    s=0
    for i in range(1,m+n,1):
        s+=i
    return s
print(FN(5))
print(FN(5,1))

def FN2(n,m=1,k=2):
    s=0
    for i in range(1,m+n+k,1):
        s+=i
    return s
print("="*30)
print(FN2(5))
print(FN2(5,3))
print(FN2(5,3,1))
print(FN2(5,k=4 ))

lst=["Vu","Xuan","Canh"]
for item in lst:
    print(item,end='\t')