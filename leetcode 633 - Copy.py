import math
def judgesquare(c:int):
    sq=int(math.sqrt(c))
    for i in range(sq+1):
        b=math.sqrt(c-(i*i))
        if b==int(b):
            return True
    return False
print(judgesquare(5))

