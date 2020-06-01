import operator
def anagram(string1, string2):
    hm1 = {} 
    hm2 = {}
    for i in string1:
        if hm1.has_key(i):
            hm1[i] +=1
        else:
            hm1[i] = 1
    for i in string2:
        if hm2.has_key(i):
            hm2[i] +=1
        else:
            hm2[i] = 1
    #hm1 = sorted(hm1.items(), key=operator.itemgetter(0))
    #hm2 = sorted(hm2.items(), key=operator.itemgetter(0))
    if hm1 == hm2:
        return True
    else:
        return False
string1 = 'LISTEN'
string2 = 'SILENT'
print (anagram(string1, string2))