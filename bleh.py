def reverseInGroups(arr, N, K):
    arr1=[]
    for i in range(0,K):
        arr1.append(arr[K-i-1])
    for j in range(K,N):
        arr1.append(arr[N-K-j])
    
    return arr1

print(reverseInGroups([1,2,3,4,5], 5, 3))