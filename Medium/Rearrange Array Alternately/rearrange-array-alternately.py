#User function Template for python3
class Solution:

    def rearrange(self,arr, n): 

        fst=0
        lst=n-1
        maxi=arr[lst]+1
        for i in range(n):
            if i%2==0:
                arr[i]+=(arr[lst]%maxi)*maxi
                lst-=1
            else:
                arr[i]+=(arr[fst]%maxi)*maxi
                fst+=1
        for i in range(n):
            arr[i]//=maxi


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