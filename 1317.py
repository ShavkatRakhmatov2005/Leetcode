n=11
new=[]
for i in range(1,n+1):
    a=i
    b=n-i
    if not '0' in str(a) and not '0' in str(b):
        if a+b==n:
            new.append(a)
            new.append(b)
            break
print(new)
