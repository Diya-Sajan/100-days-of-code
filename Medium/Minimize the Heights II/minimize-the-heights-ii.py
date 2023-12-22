#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        diff=arr[-1]-arr[0]
        mx=0
        mn=0
        for idx,val in enumerate(arr):
            if idx==0 or val<k or arr[-1]<k:
                continue
            mx=max(arr[idx-1]+k,arr[-1]-k)
            mn=min(arr[0]+k,val-k)
            diff=min(diff,abs(mx-mn))
        return diff   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends