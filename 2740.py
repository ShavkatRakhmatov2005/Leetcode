nums = [1,3,2,4]
nums.sort()
new=nums[-1]
for i in range(len(nums)-1):
    new=min(new,(abs(nums[i]-nums[i+1])))
print(new)