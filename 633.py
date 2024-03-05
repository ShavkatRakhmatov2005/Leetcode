import math
c=5
l,r=0,int(math.sqrt(c))
while l<=r:
    summ=l**2+r**2
    if summ>c:
        r-=1
    elif summ<c:
        l+=1
    else:
        print(True)
        exit()
print(False)
exit()