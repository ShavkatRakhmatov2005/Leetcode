def maxSum(nums:list):
    max_sum=-1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max_i=max(str(nums[i]))
            max_j=max(str(nums[j]))
            if max_i==max_j:
                sum_pair=nums[i]+nums[j]
                max_sum=max(max_sum,sum_pair)
    return max_sum
print(maxSum([51,71,17,24,42]))