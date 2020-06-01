a = [2,4,3,1,5]
maxi = a[1] if a[1]>a[0] else a[0]
second = a[0] if a[1] > a[0] else a[1]
for i in a[2:]:
    if i> maxi:
        second = maxi
        maxi = i
        
    elif i>second:
        second = i
