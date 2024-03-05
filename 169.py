def majorityElement(nums: list) -> int:
        return max(set(nums),key=lambda x:nums.count(x))
sonlar = [2,2,1,1,1,1,1,2,2]
print(majorityElement(sonlar))