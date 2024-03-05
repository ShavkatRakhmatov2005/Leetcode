nums = [0,2]
n=[]
if len(nums)==1:
    print(nums[0])
else: 
    for i in range(len(nums)):
        print(nums[i])
        n.append(nums[i]*nums[i+1])
print(n)