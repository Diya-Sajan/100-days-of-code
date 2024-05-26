//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {

  public:
    int lcs(string &x, string &y, int m, int n, vector<vector<int>> &dp)
    {
        if(m < 0 || n < 0)
            return 0;
        if(dp[m][n] != -1)
            return dp[m][n];
        int  a = 0;
        if(x[m] == y[n])
        {
            a = 1 + lcs(x, y, m-1, n-1, dp);
        }
        else
        {
            a = max(lcs(x, y, m, n-1, dp), lcs(x, y, m-1, n, dp));
        }
        return dp[m][n] = a;
    }
    int findMinCost(string x, string y, int costX, int costY) 
    {
        int m = x.size() - 1;
        int n = y.size() - 1;
        vector<vector<int>> dp(m+1, vector<int>(n+1,-1));
        int  len = lcs(x, y, m, n, dp);
        int ans = (x.size() - len)*costX + (y.size() - len)*costY;
        //cout << res << endl;
        return ans;
        // Your code goes here
    }
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    while (t--) {
        string x, y;
        cin >> x >> y;

        int costX, costY;
        cin >> costX >> costY;

        Solution ob;
        cout << ob.findMinCost(x, y, costX, costY);
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends