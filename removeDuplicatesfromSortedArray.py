array = [1,1,1,2,2,3,4,4,5]
i = 0
for j in range(1,len(array)):
    if(array[j] != array[i]):
        i+=1
        array[i] = array[j]
print i+1
array = [1,1,1,2,2,3,4,4,5]

count = 0
for i in range(len(array)-1):
    if array[i] == array[i+1]:
        count +=1
print(len(array)-count)
        