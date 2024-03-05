raqamlar = [8,1,2,2,3]
#count=0
new=[]
for i in range(len(raqamlar)):
    count=0
    for j in range(len(raqamlar)):
        if raqamlar[i]>raqamlar[j]:
            count+=1
    new.append(count)
print(new)