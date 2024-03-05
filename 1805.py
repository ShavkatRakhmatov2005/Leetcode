import re
word = "a1b01c001"
new=re.findall("\d+",word)
# print(set(list(map(int,new))))
# butun_sonlar = [int(x) for x in word.split() if x.isdigit()]
# print(len(butun_sonlar))
# n=list(filter(lambda x :int(x) if x.isdigit() else None,word))
# print(n)
# for i in word:
#     if i.isdigit():
#         new.append(i)
#     else:
#         new2.append(i)
# print(" ".join(new),new2)


print('hello'[0])