import collections

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[3,3]]

graph = collections.defaultdict(list)
for i, x in enumerate(stones):
    for j in xrange(i):
        y = stones[j]
        #print "i y",i,str(y)
        
        if x[0]==y[0] or x[1]==y[1]:
            #print i,j
            graph[i].append(j)
            graph[j].append(i)

N = len(stones)
ans = 0

seen = [False] * N
for i in xrange(N):
    if not seen[i]:
        print i
        stack = [i]
        seen[i] = True
        while stack:
            ans += 1
            #print ans
            node = stack.pop()
            for nei in graph[node]:
                if not seen[nei]:
                    stack.append(nei)
                    seen[nei] = True
        ans -= 1
        print ans
#print ans

#for i in range(len(graph)):
#    print i,graph[i]