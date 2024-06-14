#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        res =0
        for i in str(n):
            res+=int(i)**3
        if res==n: return 'true'
        return 'false'
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends