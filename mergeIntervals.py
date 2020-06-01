a = [[1,3],[2,6],[8,10],[15,18]]
a.sort()

re = []
re.append(a[0])
for i in range(1,len(a)):
    print a[i]
    if a[i][0] > re[-1][1]:
        re.append(a[i])
    else:
        re[-1][1] = max(re[-1][1], a[i][1])
