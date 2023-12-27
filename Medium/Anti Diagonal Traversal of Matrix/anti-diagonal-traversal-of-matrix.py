#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        
        result = []
        n = len(matrix)

        for d in range(n + n - 1):
            cd = []   # current_diagonal
            for i in range(max(0, d - n + 1), min(d, n - 1) + 1):
                j = d - i
                cd.append(matrix[i][j])
            result.extend(cd)
            
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends