def findMissingAndRepeatedValues(grid: list):
        lst=[]
        new=[]
        uniqueList=[]
        for i in grid:
            lst.extend(i)
        for i in lst:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in new:
                new.append(i)
        for i in range(1,len(lst)+1):
            if not i in lst:
                new.append(i)
        return new
grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))
