a=5
b=7
"""
if a!=b:
    c=113
else:
    c=115
print(c)

d=113 if a!=b else 115
print(d)
"""
x=int(input("Nhập một số:"))
print("Chẵn" if x%2 ==0 else "Lẻ")