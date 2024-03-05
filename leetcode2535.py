nums = [1,15,6,3]
new=[]
for i in nums:
    for j in str(i):
        new.append(int(j)) 
print(sum(nums)-sum(new))