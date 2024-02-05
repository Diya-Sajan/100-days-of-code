//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    public:
    bool canGo(int row, int col, vector<vector<int> > &m, int n){
        return row >= 0 && col >= 0 && row < n && col < n && m[row][col] != 0;
    }
    void helper(vector<string> &ans, string str, int row, int col, vector<vector<int> > &m, int n){
        if(m[row][col] == 0) return;
        if(row == n-1 && col == n-1){
            ans.push_back(str);
            return;
        }
        
        m[row][col] = 0;
        
        if(canGo(row-1, col, m, n)){
            str.push_back('U');
            helper(ans, str, row-1, col, m, n);
            str.pop_back();
        }
        if(canGo(row, col+1, m, n)){
            str.push_back('R');
            helper(ans, str, row, col+1, m, n);
            str.pop_back();
        }
        if(canGo(row+1, col, m, n)){
            str.push_back('D');
            helper(ans, str, row+1, col, m, n);
            str.pop_back();
        }
        if(canGo(row, col-1, m, n)){
            str.push_back('L');
            helper(ans, str, row, col-1, m, n);
            str.pop_back();
        }
        
        m[row][col] = 1;
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        vector<string> ans;
        helper(ans, "", 0, 0, m, n);
        return ans;
    }
};
    


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends