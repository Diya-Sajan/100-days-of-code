#User function Template for python3

class Solution:
    def findSingle(self, n, arr):
        f = []
        for i in arr:

            if i not in f:
                f.append(i);
            else:
                f.remove(i);
        
        return f[0]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends