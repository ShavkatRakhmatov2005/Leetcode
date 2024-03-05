names = ["Mary","John","Emma"]
heights = [180,165,170]
lst=[]
new=[]
for i in range(len(names)):
    lst.append([names[i],heights[i]])
lst=sorted(lst,key=lambda x :x[1],reverse=True)
for i in lst:
    new.append(i[0])
print(new)
