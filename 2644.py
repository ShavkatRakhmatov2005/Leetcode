nums = [20,14,21,10]
divisors = [5,7,5]

n=[]
for d in divisors:
    count=sum(1 for i in nums if i%d==0)
print(count)
