//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
  public:
    // Function to find the number of islands.
    int numIslands(vector<vector<char>>& grid) 
    {
      
      queue<pair<int,int>> q;
     int n=grid.size();
     int m=grid[0].size();
     int cnt=0;
     vector<vector<int>> visited(n,vector<int>(m,0));
      for(int row=0;row<grid.size();row++)
      {
          for(int col=0;col<grid[row].size();col++)
          {
              if(grid[row][col]=='1' && !visited[row][col])
              {
                  cnt++;
                   q.push({row,col});
                   visited[row][col];
                   while(!q.empty())
                 {
                   int x=q.front().first;
                   
                   int y=q.front().second;
                 
                   q.pop();
                   for(int i1=-1;i1<=1;i1++)
                   {
                       for(int j1=-1;j1<=1;j1++)
                       {
                           x=x+i1;
                           y=y+j1;
                           if(((x>=0 && x<n)  && (y>=0 && y<m)) && ((!visited[x][y]) && (grid[x][y]=='1')))
                           {
                               q.push({x,y});
                               visited[x][y]=1;
                           }
                          x=x-i1;
                          y=y-j1;
                       }
                   }
                   
                 }
              }
             
              
           }
      }
      
      return cnt;
    }
};



//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends