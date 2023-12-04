#User function Template for python3

def multiply (arr, n) : 
    sum1 = 0
    sum2 = 0
    for i in range(0,n):
        if i<n//2:
            sum1 += arr[i]
        else:
            sum2 += arr[i]
    return sum1*sum2



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends