triangle = [[-1],[2,3],[1,-1,-3]]
n=[]
for i in triangle:
    print(min(i))
    n.append(min(i))
print(sum(n))