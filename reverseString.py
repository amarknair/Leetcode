def reverseString(string):
    string = list(string)
    length = len(string)
    for i in range(length/2):
        temp = string[i]
        string[i] = string[length-i-1]
        string[length-i-1] = temp
    string = ''.join(string)
    return(string)
    
string = "Hello"
print reverseString(string)