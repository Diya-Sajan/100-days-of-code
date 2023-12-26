class Solution:
    def merge(self, arr, l, mid, r):
        n1 = (mid-l)+1 # left size
        n2 = (r-mid) # right size
        left = []
        right = []
        
        k=l
        for i in range( n1):
            left.append(arr[k])
            k+=1
        
        for j in range(n2):
            right.append(arr[k])
            k+=1
        
        inv_count=0
        i = 0
        j = 0
        k=l
        while (i < n1) and (j < n2):
            if left[i] <= right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
                inv_count+= (n1-i) #OR len(left)-i # ***IMP
            k+=1
        
        while i < n1:
            arr[k]=left[i]
            k+=1
            i+=1
        
        while j < n2:
            arr[k]=right[j]
            k+=1
            j+=1
            
        return inv_count
        
    
    def merge_sort(self, arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left+right)//2
            inv_count += self.merge_sort(arr, left, mid)
            inv_count += self.merge_sort(arr, mid+1, right)
            inv_count += self.merge(arr, left, mid, right)
        return inv_count
    
    

    def inversionCount(self, arr, n):
        # Your Code Here
        left = 0
        right = n-1
        return self.merge_sort(arr, left, right)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends