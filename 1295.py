nums = [555,901,482,1771]
n=[]
for i in nums:
    count=0
    for j in str(i):
        count+=1
    n.append(count)
count=0
for i in n:
    if not i%2:
        count+=1
print(count)