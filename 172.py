n=7

sum=1
count=0
for i in range(1,n+1):
    sum*=i
print(str(sum)[::-1])
for j in str(sum)[::-1]:
    if i!=0:
        break
    else:
        count+=1
print(count)