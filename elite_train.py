import os
os.system("clear")

n = 5
k = 2
m = 4

lst = [[0, 4], [1, 2], [1, 4], [2, 4]]
nat = [0] * n

i = 0
while i < len(lst):
    check = True
    j = lst[i][0]
    while j < lst[i][1] + 1:
        if j < len(nat)-1 and nat[j] > nat[j + 1]:
            lst[i][0] += 1
        else:
            if k > nat[j]:
                nat[j] += 1
            else:
                check = False
                break
        # print(" " * 4, nat, j)
        j += 1
        
    i += 1
    print(int(check))
