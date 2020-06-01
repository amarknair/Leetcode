arr = [3,4,-1,0,10,4,1,2,5]

arr.append(0)
n = len(arr)
for i in range(len(arr)):
    if arr[i]>=n or arr[i] < 0:
        arr[i] = 0

for i in range(len(arr)):
    arr[arr[i]] = arr[arr[i]]%n  

print arr
