def likes(names:list):
    if not names:
        return f"No on like this"
    elif len(names)==1:
        return f"{names[0]} like this"
    elif len(names)==2:
        return f"{names[0]} and {names[1]} like this"
    else:
        return f"{', '.join(names[:-1])} and {names[-1]} likes this"
n=["Max","John","Dilshod"]
print(likes(n))