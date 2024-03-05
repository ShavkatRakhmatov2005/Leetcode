nums = [10,4,8,3]
res=[]
for i in range(len(nums)):
    res.append(abs(sum(nums[:i])-(sum(nums[i+1:]))))
print(res)
   