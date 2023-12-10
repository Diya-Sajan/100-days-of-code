class Solution:
    def findUnique(self, a, n, k): 
        f = {}
        for i in a:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        for j in f:
            if f[j]%k!=0:
                return j
        return 0    


#{ 
 # Driver Code Starts
import sys 

if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        n,k=[int(x) for x in input().split()]
        a = [int(x) for x in input().split()]

        print(Solution().findUnique(a,n,k))
# } Driver Code Ends