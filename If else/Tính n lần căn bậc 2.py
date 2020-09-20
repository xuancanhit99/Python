#Nhập n. Tính S(n)=sqrt(2+sqrt(2+sqrt(2+...+sqrt(2))))
#Có n dấu căn lồng nhau
from math import sqrt

n=int(input("Nhập n = "))
S=sqrt(2)
for i in range(2,n+1):
    S=sqrt(2+S)
print("S({0}) = {1}".format(n,S))