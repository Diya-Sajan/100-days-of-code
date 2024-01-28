#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def ceilIdx(self,tail,x):
        l=0
        r=len(tail)
        while l<r:
            m=l+(r-l)//2
            if tail[m]>=x:
                r=m
            else:
                l=m+1

        return r
    
    def longestSubsequence(self,a,n):
        # code here
        n=len(a)
        tail=[a[0]]
        for i in range(1,n):
            if a[i]>tail[-1]:
                tail.append(a[i])
            else:
                c=self.ceilIdx(tail, a[i])
                tail[c]=a[i]
        return len(tail)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends