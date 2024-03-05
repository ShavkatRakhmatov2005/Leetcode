num=14
count=0
while num==0:
    if not num%2:
        num=num//2
    if num%2:
        num=num-1
    count+=1
print(count)