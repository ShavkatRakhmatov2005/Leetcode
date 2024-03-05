title = "capiTalIze te titLe"
s=[]
for i in title.split():
    if len(i)>2:
        s.append(i.capitalize())
    else:
        s.append(i.lower())
new=" ".join(s)
print(new)
