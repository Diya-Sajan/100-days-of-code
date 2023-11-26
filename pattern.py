def pattern(N):
    if N <= 0:
        return [N,]
    a = list(range(N, -5, -5))    
    return a + a[::-1][1:]

print(pattern(23))