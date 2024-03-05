from collections import Counter
nums = [1,2,1,3,2,5]
new=[]
n=Counter(nums)
for x,y in n.items():
    if y==1:
        new.append(x)
print(new)

# dct={}
# n=[]
# m=[]
# for i in nums:
#     dct[i]=nums.count(i)
# for j in dct.items():
#     n.append(list(j))
# for k in n:
#     if k[1]==1:
#         m.append(k[0])
# print(m)