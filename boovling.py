n=int(input("N= "))
lst=list(range(1,n+1))

k=int(input("K= "))

for i in range(k):
    x,y=list(map(int,input().split()))
    for j in range(x,y+1):
        if j in lst:
            lst[lst.index(j)]="*"
for i in range(len(lst)):
    if lst[i]!="*":
        lst[i]="|"
print(" ".join(lst))