#User function Template for python3

class Solution:
    def countLessEqual(self, row, target):
        # Binary search to count the number of elements less than or equal to the target in a row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def median(self, matrix, R, C):
        # Define the search space for median
        min_val, max_val = float('inf'), float('-inf')
        for row in matrix:
            min_val = min(min_val, row[0])
            max_val = max(max_val, row[-1])
        # Binary search for median value
        while min_val < max_val:
            mid_val = min_val + (max_val - min_val) // 2
            count = 0
            for row in matrix:
                count += self.countLessEqual(row, mid_val)
            if count <= (R * C) // 2:
                min_val = mid_val + 1
            else:
                max_val = mid_val
        return min_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends