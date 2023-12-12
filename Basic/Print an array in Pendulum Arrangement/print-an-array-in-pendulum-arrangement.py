#User function Template for python3

def pendulumArrangement( arr, n):
    id
    ar = []
    arr = sorted(arr)
    for i in range(n-1,-1,-1):
        if i %2 == 0:
            ar.append(arr[i])
    for i in range(0, n):
        if i %2 != 0:
            ar.append(arr[i])

    return ar


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        answer = pendulumArrangement(arr, n)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends