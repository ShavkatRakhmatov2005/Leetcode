from collections import deque
temperatures = [30,40,50,60]
temperature=deque(temperatures)
count=0
n=[]
ans=0
for i in range(len(temperature)):
    count=0
    if temperature[i]>ans:
        ans=temperature[i]
        count+=1

        print(count)
#         n.append(count)
#         i+=1
# # temperature.popleft()
# print(temperature,n)