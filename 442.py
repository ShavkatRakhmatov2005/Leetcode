from collections import Counter
nums = [4,3,2,7,8,2,3,1]
x=Counter(nums)
n=[]
# print(x)
for i,j in x.items():
    if j>=2:
        n.append(i)
print(n)