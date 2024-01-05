#User function Template for python3

class Solution:
	def TotalWays(self, n):
    
        mod = 10**9+7
        x, y = 1, 2 
           
        for i in range(2, n+1):
            
            z = y
            z += x
            z %= mod
            
            x, y = y, z
         
        return (y**2)%mod   


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends