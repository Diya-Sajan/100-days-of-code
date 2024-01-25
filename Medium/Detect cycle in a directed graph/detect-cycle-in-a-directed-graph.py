#User function Template for python3

class Solution:
   has_cycle = False
   # Function to detect cycle in a directed graph.
   def isCyclic(self, V, adj):
       visited = {}

       # there is a cycle if vertex is in current dfs call
       dfs_visited = {} 
       self.has_cycle = False
       
       for i in range(V):
           if(i not in visited):
               self.dfs(i, adj, visited, dfs_visited)
       
       return self.has_cycle
   
   def dfs(self, vertex, adj, visited, dfs_visited):
       if(vertex in dfs_visited):
           self.has_cycle = True
           return
       
       if(vertex not in visited):
           
           for x in adj[vertex]:
               visited[vertex] = 1
               dfs_visited[vertex] = 1
               self.dfs(x, adj, visited, dfs_visited)
               del dfs_visited[vertex]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends