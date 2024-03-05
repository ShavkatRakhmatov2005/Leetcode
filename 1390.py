from math import sqrt
raqamlar = [21,4,7]
raqamlar=set(raqamlar)
raqamlar.i
sum1=0
for raqam in raqamlar:
    divisor=set()
    for i in range (1,int(sqrt(raqam))+1):
        if raqam%i==0:
            divisor.add(raqam//i)
            divisor.add(i)
            print(divisor)
            if len(divisor)>4:
                break
    if len(divisor)==4:
        sum1+=sum(divisor)
print(sum1)
    
    
