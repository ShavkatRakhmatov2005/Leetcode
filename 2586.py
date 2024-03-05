words =["vo","j","i","s","i"]
words=set(words)
s=['a','e','i','o','u']
count=0
for i in words:
    if i[0] in s and i[-1] in s:
        count+=1
print(count)