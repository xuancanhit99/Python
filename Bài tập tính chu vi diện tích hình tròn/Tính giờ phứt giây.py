t=int(input("Input second t="))
h=(t//3600)%24
m=(t%3600)//60
s=(t%3600)%60
f="AM"
if h>12:
    h=h-12
    f="PM"
print(h,':',m,":",s, f)

print('{0}:{1}:{2} {3}'.format(h, m, s, f))