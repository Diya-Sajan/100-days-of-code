#User function Template for python3
class Solution:
    def maxProduct(self,arr, n):
        if not arr:
            return 0
        # Initialize variables to keep track of max and min product ending at each position
        pref = arr[0]
        suff = arr[0]
        max_product = arr[0]
 
        for num in arr[1:]:
            # If the current number is negative, swap max and min products
            if num < 0:
                pref, suff = suff, pref
            # Update max and min products ending at the current position
            pref = max(num, pref * num)
            suff = min(num, suff * num)
 
            # Update the global maximum product
            max_product = max(max_product, pref)
 
        return max_product


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends