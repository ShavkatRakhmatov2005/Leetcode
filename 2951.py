m = [1,4,4]
n=[]
for i in range(1,len(m)-1):
    if m[i]>m[i-1] and m[i]>m[i+1]:
        print(m[i])
        
                  