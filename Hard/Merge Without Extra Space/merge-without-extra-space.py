#User function Template for python3
from math import ceil


class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        gap = ceil((n+m)/2)
        while gap > 0:
            i = 0
            j = gap
            
            
            while j < (n+m):
                
                #i,j lies in arr1
                if j  <= (n-1):
                    if arr1[i] > arr1[j]:
                        arr1[i], arr1[j] = arr1[j], arr1[i]
                    i+=1
                    j+=1
                elif i >= n: # i and j lies in arr2
                    if arr2[i-n] > arr2[j-n]:
                        arr2[i-n], arr2[j-n] = arr2[j-n], arr2[i-n]
                    i+=1
                    j+=1
                else: # i in arr1 and j in arr2
                    if arr1[i] > arr2[j-n]:
                        arr1[i], arr2[j-n] = arr2[j-n], arr1[i]
                    i+=1
                    j+=1
            
            if gap == 1:
                break
            gap = ceil(gap/2)

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends