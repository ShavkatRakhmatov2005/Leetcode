nums = [13,2,25,83,77]
n="".join(str(nums))
new=[]
for i in n:
    if i.isdigit():
        new.append(i)
print(new)