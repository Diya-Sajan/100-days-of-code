class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        maxi = A[-1]
        ar=[maxi]
        
        for i in range (N-2,-1,-1):
            
            if A[i]>=A[i+1] and A[i] >= maxi:
                maxi = A[i]
                ar.append(maxi)
        

        ar[:]=ar[::-1]
        return ar
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends