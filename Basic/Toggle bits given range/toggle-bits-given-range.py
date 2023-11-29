#User function Template for python3

class Solution:
    def toggleBits(self, N , L , R):
        res = (1<<(L-1))-1
        res1 = (1<<R)-1
        temp=res^res1
        return N^temp



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.toggleBits(N,L,R))
# } Driver Code Ends