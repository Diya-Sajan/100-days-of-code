#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, s):
        dp = [1] + [0]*s
        MOD = 10**9 + 7
        for a in arr:
            for i in range(s, a-1, -1):
                dp[i] = (dp[i] + dp[i-a])%MOD
        return dp[s]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends