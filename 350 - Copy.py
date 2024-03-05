# nums1 = [1,2,2,1]
# nums2 = [2,2]
# nums1=set(nums1)
# nums2=set(nums2)
# nums1.intersection(nums2)
# print(nums1)
# import Counter from collections
from collections import Counter

# creating a raw data-set
x = Counter ("geeksforgeeks")

# will return a itertools chain object
# which is basically a pseudo iterable container whose
# elements can be used when called with a iterable tool
print(list(x.elements()))

