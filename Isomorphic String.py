s = "egg"
t = "add"

print "isomorphic" if [s.find(i) for i in s] == [t.find(j) for j in t] else "non isomorphic"