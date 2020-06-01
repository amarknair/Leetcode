a = [False for i in range(26)]
string = "tests"
duplicate = 0
for i in string:
    temp = ord(i) - 96
    if a[temp] == False:
        a[temp] = True
    else:
        duplicate +=1
print duplicate
    