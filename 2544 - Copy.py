n=886996
sum=0
new=list(map(str,str(n)))
for idx,i in enumerate(new):
    if idx%2:
        sum=sum-int(i)
    else:
        sum=sum+int(i)
        
print(sum)
    