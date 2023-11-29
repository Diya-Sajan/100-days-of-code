def setKthBit(N, K):
    num = bin(N)[2:]
    k=len(num)-(K+1)
    res = num[:k]+'1'+num[k+1:]
    return int(res,2)
    

setKthBit(10, 2)