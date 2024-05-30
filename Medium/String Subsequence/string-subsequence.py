
from functools import lru_cache
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        n,m,MOD=len(s1),len(s2),1000000007
        
        pre=[0]*(m+1)
        pre[m]=1
        for i in range(n-1,-1,-1):
            curr=[0]*(m+1)
            curr[m]=1
            for j in range(m-1,-1,-1):
                ans=pre[j]%MOD
                if s1[i]==s2[j]:
                    ans+=pre[j+1]%MOD
                curr[j]=ans%MOD
            pre=[k for k in curr]
        return curr[0]%MOD
        
        # RECURSION + MEMOIZATION:
        #
        # @lru_cache(None)
        # def fun(i,j):
        #     nonlocal n,m,MOD
        #     if j==m:
        #         return 1
        #     if i==n:
        #         return 0
        #     ans=fun(i+1,j)%MOD
        #     if s1[i]==s2[j]:
        #         ans+=fun(i+1,j+1)%MOD
        #     return ans%MOD
        # return fun(0,0)
        
        
        # TABULATION:
        #
        # dp=[[0]*(m+1) for _ in range(n+1)]
        # dp[n][m]=1
        # for i in range(n-1,-1,-1):
        #     dp[i][m]=1
        #     for j in range(m-1,-1,-1):
        #         ans=dp[i+1][j]%MOD
        #         if s1[i]==s2[j]:
        #             ans+=dp[i+1][j+1]%MOD
        #         dp[i][j]=ans%MOD
        # return dp[0][0]%MOD




#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends