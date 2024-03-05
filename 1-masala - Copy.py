s=[-1,2,3,-1,-2]
n=[]
m=[]
for i in range(len(s)-1):
    if s[i]>0 and s[i+1]>0:    
         n.append(s[i])
         n.append(s[i+1])
         n.append('\n')
    elif s[i]<0 and s[i+1]<0:
        m.append(s[i])
        m.append(s[i+1])
        m.append('\n')
print(*n,*m)

