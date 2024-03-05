nums = [5,6]
k = 6
n=[]
for i in range(1,k+1):
    if i in nums:
       i+=1
    else:
        n.append(i)
print(n)
