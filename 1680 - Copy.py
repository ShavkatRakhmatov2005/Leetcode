n=12
lst=[]
new=""
for i in range(1,n+1):
    lst.append(i)
for i in lst:
    new+=(bin(i)[2:])
print(int(new,2))