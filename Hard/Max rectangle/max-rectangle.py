#User function Template for python3


class Solution:
    def maxArea(self, M, n, m):
        def max_area_histogram(heights):
            stack = []
            max_area = 0
            index = 0
            while index < len(heights):
                if not stack or heights[index] >= heights[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    top_of_stack = stack.pop()
                    area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                    max_area = max(max_area, area)
            while stack:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
            return max_area

        max_area = 0
        heights = [0] * m
        for row in M:
            for i in range(m):
                heights[i] = heights[i] + 1 if row[i] == 1 else 0
            max_area = max(max_area, max_area_histogram(heights))
        return max_area

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends