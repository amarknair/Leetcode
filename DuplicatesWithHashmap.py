from collections import defaultdict
import operator
hashmap = {}
string = "test"
for i in string:
    if hashmap.has_key(i):
        hashmap[i] +=1
    else:
        hashmap[i] = 1
for key in hashmap:
    print key, hashmap[key]
#-----------------------------------------#
hashmap['k'] = 5
#hashmap = defaultdict(hashmap)
#hashmap.OrderedDict(sorted(hashmap.keys))
hashmap = sorted(hashmap.items(), key=operator.itemgetter(1))

#hashmap = sorted(hashmap.items(), key = operator.itemgetter(1))    
