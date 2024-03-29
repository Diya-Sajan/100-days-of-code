//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int maxGold(int n, int m, vector<vector<int>> M)
    {
       int ans=0;
       for(int col=m-2;col>=0;--col)
       {
           for(int row=0;row<n;++row)
           {
               int right_up=(row==0)?0:M[row-1][col+1];
               int right=M[row][col+1];
               int right_down=(row==n-1)?0:M[row+1][col+1];
               M[row][col]=max(right_up,max(right,right_down))+M[row][col];
           
           }
       }
       for(int i=0;i<n;++i)
       {
           ans=max(ans,M[i][0]);
       }
       return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        vector<vector<int>> M(n, vector<int>(m, 0));
        for(int i = 0;i < n;i++){
            for(int j = 0;j < m;j++)
                cin>>M[i][j];
        }
        
        Solution ob;
        cout<<ob.maxGold(n, m, M)<<"\n";
    }
    return 0;
}
// } Driver Code Ends