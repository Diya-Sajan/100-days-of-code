#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        sum1 = 0
        sum2 = 0
        for i in range(0,n):
            if i<n//2:
                sum1 += a[i]
            else:
                sum2 += a[i]
        return abs(sum1-sum2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends