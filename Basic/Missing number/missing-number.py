#User function Template for python3

def missingNumber( A, N):
    sum=0
    a=(N*(N+1))//2
    for i in range(0,N-1):
        sum+=A[i]
    return a-sum
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends