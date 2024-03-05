# # Python3 Program to Sort list of
# # integers according to sum of digits

# def sortList(lst):
# 	digits = [int(digit) for digit in str(lst) ]
# 	print(sum(digits))
# 	return sum(digits)
	
# # Driver Code
# lst = [12, 10, 106, 31, 15]
# print(sorted(lst, key = sortList))
def sortList(lst):
	return sorted(lst, key = lambda x:(sum(map(int, str(x)))))
    

lst = [20, 10, 106, 31, 15]
print(sortList(lst))