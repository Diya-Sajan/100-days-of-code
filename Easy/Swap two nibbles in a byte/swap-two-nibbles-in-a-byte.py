#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        right = (n&15)
        right = (right<<4)
        left = (n&240)
        left = (left >> 4)
        ans = (right|left)
        return int(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends