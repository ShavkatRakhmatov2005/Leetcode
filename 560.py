nums = [-1,-1,1]
k = 1

count=0
for i in range(len(nums)-1):
    if nums[i]+nums[i+1]==k or nums[-1]==k:
        count+=1
print(count)