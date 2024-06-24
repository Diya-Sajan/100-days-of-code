#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        start = 2
        end = 2 * n
        mid = n+1
        
        if q == 1:
            return 0
        if q > end:
            return 0
        
        if q == mid:
            return n
        elif q >= 2 and q < mid:
            return q-1
        else:
            num = q - mid # 7 - 6 = 1
            return mid -1 - num
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends