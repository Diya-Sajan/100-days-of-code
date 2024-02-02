#User function template for Python

class Solution:
    def atoi(self,s):
        try:
            return int(s)
        except Exception:
            return -1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends