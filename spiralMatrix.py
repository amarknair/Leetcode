a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
m = len(a)
n = len(a[0])
k = 0
l = 0
output = []
while(k<m and l<n):
    temp =[]
    for i in range(l,n):
        print a[k][i]
        output.append(a[k][i])
    k +=1
    for i in range(k,m):
        print(a[i][n-1])
        output.append(a[i][n-1])
    n-=1
    if(k<m):
        for i in range(n-1,l-1,-1):
            print(a[m-1][i])
            output.append(a[m-1][i])
    m-=1
    if(l<n):
        for i in range(m-1,k-1,-1):
            print(a[i][l])
            output.append(a[i][l])
    l+=1