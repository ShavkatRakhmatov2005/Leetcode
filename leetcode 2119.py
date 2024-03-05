# num=526
# rev=0
# while num!=0:
#     rev=rev*10+(num%10)
#     num//=10
# print(rev)
# def isSameAfterReversals(num: int) -> bool:
#         rev=0
#         while num!=0:
#             rev=rev*10+(num%10)
#             num//=10
#         if len(str(num))==len(str(rev)):
#             return True
#         else:
#             return False
# print(isSameAfterReversals(526))
def isSameAfterReversals( num: int) -> bool:
    return len(str(num))==len(str(int(str(num)[::-1])))
print(isSameAfterReversals(526))