s = "Let's take LeetCode contest"
# n="".join(list(map(str,s[::-1])))
# print(n)
s = s.split()
revers =" ".join(i for i in list(map(lambda st: st[::-1],s)))
print(revers)