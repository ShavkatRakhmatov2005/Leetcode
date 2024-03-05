arr = [4,-2,2,-4]
s=[]
n=[]
for i in range(len(arr)):
    if arr[i]<0:
        s.append(arr[i])
    else:
        n.append(arr[i])
print(s,n)
