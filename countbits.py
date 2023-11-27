def countBitsFlip(a,b):
    
    A = [*bin(a)][2:]
    B = [*bin(b)][2:]

    if len(A)> len(B):
        x = len(A) - len(B)
        B = ['0']*x + B
    elif len(A)< len(B):
        x = len(B) - len(A)
        A = ['0']*x + A
    count = 0
    print(A,B)
    for i in range(0,len(A)):
        if A[i]!=B[i]:
            count+=1
    return count


print(countBitsFlip(0,1023))