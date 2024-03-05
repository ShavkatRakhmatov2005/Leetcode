purchase=15
qoldiq=purchase%10
if qoldiq<5:
    purchase-=qoldiq
else:
    purchase+=(10-qoldiq)
print(100-purchase)

