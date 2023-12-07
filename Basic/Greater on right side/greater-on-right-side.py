#User function Template for python3
class Solution:
     
    def nextGreatest(self,arr, n):
        max_right=-1
         
        for i in range(n-1,-1,-1):
            current_value=arr[i]
            arr[i]=max_right
            max_right=max(max_right,current_value)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.nextGreatest(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends