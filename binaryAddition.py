a = [1,1,1]
b= [0,0,1]
carry = 0
index = 0
result = ''
while(index<max(len(a), len(b))):
    num_a = a[-1-index] if index< len(a) else 0
    numb_b = b[-1-index] if index< len(b) else 0
    val = num_a + numb_b + carry
    carry = 1 if val>1 else 0
    val = val%2
    result = str(val) + result
    index +=1
if carry == 1:
    result = '1' + result