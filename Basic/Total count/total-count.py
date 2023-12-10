#User function Template for python3

class Solution:
    def totalCount(self, arr, n, k):
        count = 0
        for i in arr:
            if i%k ==0:
                count +=i//k
            else:
                count += ((i//k)+1)
        return count    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.totalCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends