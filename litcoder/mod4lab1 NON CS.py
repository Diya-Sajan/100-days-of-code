import sys
def frequencyCount(instring, n): 
    arr = instring.split(" ")
    for i in range(n):
        arr[i] = int(arr[i])
    arr = sorted(arr)
    print(arr)
    p = arr[n-1]   
    freq = [0] * (p+1) 
    for i in range(n): 
        if arr[i] >= 0 and arr[i] <= p: 
            freq[arr[i]] += 1
    outstring = ""
    for i in freq:
        outstring+= str(i)+" "
    return outstring

n = int(input())   
instring = input() 
outputVal = frequencyCount(instring , n)
print (outputVal)
