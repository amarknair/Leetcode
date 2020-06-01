a = [[0]*4]*4
count = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        #print count
        a[i][j] = count
        #print a[i][j]
        count += 1
    print count
for i in range(len(a)):
    for j in range(len(a[0])):
        print a[i][j]
b = [[0]*4]*4
for i in range(len(a)):
    for j in range(len(a[0])):
        b[i][j] = a[j][len(a)-1-i]
for i in range(len(a)):
    for j in range(len(a[0])):
        print b[i][j]