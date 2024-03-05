n=234
s=0
k=1
for i in str(n):
    s+=int(i)
    k*=int(i)
print(k-s)