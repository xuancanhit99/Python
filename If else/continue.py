sum=0
for n in range(1,16,2):
    if n is 3 or n is 11:
        continue
    sum+=n
print(sum)
