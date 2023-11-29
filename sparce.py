def isSparse(n):
    num = bin(n)[2:]
    print(num)
    for i in range(len(num)-1):
        if num[i]==num[i+1]:
            return 0
    return 1


print(isSparse(41))



 
