#User function Template for python3

class Solution:
    def spirallyTraverse(self, matrix, r, c):
        if r < 1 or c < 1:
            return []
        loci = [(0, j) for j in range(c)]
        loci += [(i, c - 1) for i in range(1, r)]
        loci += [(r - 1, j) for j in range(c - 2, -1, -1) if r != 1]
        loci += [(i, 0) for i in range(r - 2, 0, -1) if c != 1]
        out = [matrix[i][j] for i, j in loci]
        for i in range(r):
            matrix[i] = matrix[i][1: c - 1]
        matrix = matrix[1: r - 1]
        return out + self.spirallyTraverse(matrix, r - 2, c - 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends