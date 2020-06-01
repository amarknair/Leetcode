a = [9,9,8,9]
n = len(a)
a[n-1] += 1
carry=a[n-1]/10
a[n-1] = a[n-1]%10

for i in range(n-2,-1,-1):
    a[i]= carry + a[i]
    carry = a[i]/10
    a[i] = a[i]%10
if(a[0]==0 and carry == 1):
    a.insert(0,carry)