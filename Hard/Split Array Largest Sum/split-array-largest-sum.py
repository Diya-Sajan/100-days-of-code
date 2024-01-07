#User function Template for python3

class Solution:
    def splitArray(self, arr, n, k):
        # code here 
        low, high = max(arr), sum(arr)
        while low<high:
            mid = (low+high)//2
            currsum = 0
            cnt = 0
            for el in arr:
                currsum += el
                if currsum > mid:
                    currsum = el
                    cnt += 1
            if cnt >= k:
                low = mid + 1
            else:
                high = mid
        return high

 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends