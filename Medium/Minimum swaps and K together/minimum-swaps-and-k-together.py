#User function Template for python3

class Solution:
    def minSwap(self, arr, n, k):
        # Count the number of elements less than or equal to k
        count_k = sum(1 for num in arr if num <= k)

        # Initialize pointers and variables
        start, end = 0, 0
        currentCount = 0
        maxCount = 0

        while end < n:
            if arr[end] <= k:
                currentCount += 1

            if end - start + 1 > count_k:
                if arr[start] <= k:
                    currentCount -= 1
                start += 1

            maxCount = max(maxCount, currentCount)
            end += 1

        # Calculate the minimum number of swaps required
        minSwaps = count_k - maxCount

        return minSwaps

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends