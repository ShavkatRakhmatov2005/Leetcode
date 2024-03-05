# def findMinFibonacciNumbers( k: int) -> int:
#         if k<0:
#             return False
#         elif k==0:
#              return 0
#         elif k==1 or k==2:
#              return 1
#         else:
#             return findMinFibonacciNumbers(k-1)+findMinFibonacciNumbers(k-2)
# print(findMinFibonacciNumbers(7))
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2 
# count = 1
# lst =0
# for count in range(n):
#     #st+=next_number
# 	print(next_number, end=" ")
# 	num1, num2 = num2, next_number
# 	next_number = num1 + num2    

n = 7
result = [0,1]
while len(result) <= n:
    result.append(result[-1] + result[-2])
print(result)
for i in result:
    if i+i+1==n:
        print(i,i)