class Solution:
    def duplicates(self, arr, n):

        visited = [-1 for _ in range(n)]
        for element in arr:
            if visited[element] == -1:
                visited[element] = -10
            elif visited[element] == -10:
                visited[element] = element
        pos = 0
        for i in range(n):
            if visited[i] > -1:
                arr[pos] = i
                pos += 1
        if not pos:
            return [-1]
        for i in range(pos, n):
            arr.pop()
       
        return arr
#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends