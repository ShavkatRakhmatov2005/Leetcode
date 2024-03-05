n=input()
left='1QAZ2WSX3EDC4RFV5TGB'
right='6YHN7UJM8IK,9OL.OP:/'
l=0
r=0
for i in n.lower():
    if i in left.lower():
        l+=1
    elif i in right.lower():
        r+=1
print(f"Left={l} Right={r}")
