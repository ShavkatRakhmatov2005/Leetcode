s = "leetcode exercises sound delightful".split()
for i in range(len(s)-1):
    if s[i][-1]==s[i+1][0] and s[-2][-1] == s[-1][0]:
        print(True)
    print(False)