class Solution:
    def leftRotate(self, arr, k, n):
        kn=k%n
        if kn == 0:
            return arr
        else:
            arr[:] = arr[kn:]+arr[:kn]
            return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends