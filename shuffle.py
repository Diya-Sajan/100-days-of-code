def shuffleArray(arr, n):
    temp=[]
    for i in range(n):
        temp.append(arr[i])
    x = 0

    for i in range(0, n, 2):
        arr[i] = temp[x]
        x+=1

    for i in range(1, n, 2):
        arr[i] = temp[x]
        x+=1

        return arr

'''    new = [0]*n
    for i in range(0,n):
        if i%2 == 0:
            new[i] = arr[int(i/2)]
        elif i+1==n:
            new[i] = arr[i]
        else:
            new[i] = arr[int(n/2) + i - 1]
            
    return new
'''

print(shuffleArray([1,2,9,15],4))