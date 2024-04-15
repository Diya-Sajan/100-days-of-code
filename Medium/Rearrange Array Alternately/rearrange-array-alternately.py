#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        res = []
        if(n<=1):
            return arr
        i=1
        for i in range(1,(n//2)+1):
            res.append(arr[-i])
            res.append(arr[i-1])
        if(n%2!=0):
            res.append(arr[-(i+1)])
        
        arr[:]=res[:]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends