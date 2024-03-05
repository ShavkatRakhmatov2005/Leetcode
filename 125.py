s = "0P"
natija="".join([i.lower() if i.islower() or i.istitle() else "" for i in s])
print(natija)
# if natija==natija[::-1]:
#     print(True)
# else:
#     print(False)