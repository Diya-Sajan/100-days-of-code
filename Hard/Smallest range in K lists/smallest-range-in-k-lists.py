#User function Template for python3

from heapq import heappush, heappop
class Solution:
    def smallestRange(self, arr, n, k):
        # code here
        # print the smallest range in a new line
        hq = []
        mx = 0
        for i in range(k):
            heappush(hq, (arr[i][0], i, 0))
            mx = max(mx, arr[i][0])
        rang = float('inf')
        while len(hq) >= k:
            mi, row, col = heappop(hq)
            r = mx - mi
            if r < rang:
                rang = r
                ans = [mi, mx]
            if col + 1 < n:
                mx = max(mx, arr[row][col + 1])
                heappush(hq, (arr[row ][col + 1], row, col + 1))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends