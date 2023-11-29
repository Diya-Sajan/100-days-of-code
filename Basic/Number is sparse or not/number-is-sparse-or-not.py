#User function Template for python3

class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):

        return (n & (n >> 1)) == 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends