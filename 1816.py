def s(s:str,k:int):
    return " ".join(s.split()[:k])
n = "Hello how are you Contestant"
k=4
print(s(n,k))