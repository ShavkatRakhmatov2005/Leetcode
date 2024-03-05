nums1 = [1,2,3]
nums2 = [2,4]
new=[]
for i in nums1:
     if i in nums2:
                new.append(i)
print(*new)