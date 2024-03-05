from collections import Counter
nums = [0,1,2,2,4,4,1]
n=[]
for i in nums:
    if not i%2:
        n.append(i)
print(Counter(n))