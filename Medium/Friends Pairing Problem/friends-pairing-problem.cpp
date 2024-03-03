//{ Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends

class Solution
{
    const int mod = 1e9+7;
private:
    int solve(int n)
    {
    
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++)
        {
            long long ans = ((dp[i - 1] * 1LL % mod) + (((dp[i - 2] * 1LL % mod) * (i - 1)) % mod)) % mod;
            dp[i] = ans;
        }
        return dp[n];
    }
    
public:
    int countFriendsPairings(int n) 
    { 
        
        return solve(n);
    }
};        
 

//{ Driver Code Starts.
int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
    	int n;
    	cin>>n;
    	Solution ob;
    	cout <<ob.countFriendsPairings(n); 
    	cout<<endl;
    }
} 

// } Driver Code Ends