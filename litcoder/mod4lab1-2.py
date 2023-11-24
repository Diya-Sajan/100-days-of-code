def mixArray(n, q, arr):  
    A = [0]*n
    for i in range(0,q):
        a = int(arr[i][0])
        b = int(arr[i][1])
        num = int(arr[i][2])
        for j in range(a-1,b):
            A[j] += num
    maxval=0
    for x in A:
        if x>maxval: maxval = x    
    return maxval
n = int(input())
q = int(input())
arr=[]
for i in range(0,q):
    instring = input()
    arr.append(instring.split(" "))
print(mixArray(n, q, arr))