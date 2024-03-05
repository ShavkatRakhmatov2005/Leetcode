def pivot(n:int):
    new=[]
    for i in range(1,n+1):
        new.append(i)
    print(new)
    leftSum,rightSum=0,sum(new)
    for idx,ele in enumerate(new):
        rightSum-=ele
        if leftSum==rightSum:
            return idx
        leftSum+=ele
    return -1
print(pivot(8))
