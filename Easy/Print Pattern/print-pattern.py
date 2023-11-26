#User function Template for python3

class Solution:
    def pattern(self, N):
        if N <= 0:
            return [N,]
        a = list(range(N, -5, -5))
        return a + a[::-1][1:]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends