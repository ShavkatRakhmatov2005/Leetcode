str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
n=list(set(str2))
n.sort()
new="".join(list(map(str,n)))
print(new)