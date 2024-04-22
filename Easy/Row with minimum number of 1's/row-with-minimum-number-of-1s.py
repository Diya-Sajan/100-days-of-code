#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        res = float('inf')
        rin = 0
        for i in range(n):
            s = sum(a[i])
            #print(i , s , res)
            if s<res:
                res = s
                rin = i
            
        return rin + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends