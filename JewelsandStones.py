J = "aA"
S = "aAAbbbb"
Jset = set(J)
count = 0
for i in S:
    if i in Jset:
        count +=1
print count