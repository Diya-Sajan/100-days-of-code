#User function Template for python3

class Solution:
    def findNth(self,N):
        ans = 0
        t = 1
        while N > 0:
            ans += (t * (N % 9))
            N = N // 9
            t = t * 10
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends