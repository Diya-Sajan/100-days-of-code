//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++


class Solution
{
    public:
    //Function to find length of shortest common supersequence of two strings.
    int solver(int i,int j,string X, string Y, int m, int n,vector<vector<int>> &dp){
        
        if(i<0){
            return j+1;
        }
        
        if(j<0){
            return i+1;
        }
        
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        
        if(X[i]==Y[j]){
            return dp[i][j] = 1+solver(i-1,j-1,X,Y,m,n,dp);
        }
        else{
            return dp[i][j] = min(1+solver(i,j-1,X,Y,m,n,dp),1+solver(i-1,j,X,Y,m,n,dp));
        }
        
        
    }
    
    int shortestCommonSupersequence(string X, string Y, int m, int n)
    {
        
        vector<vector<int>> dp(m,vector<int>(n,-1));
        
        return solver(m-1,n-1,X,Y,m,n,dp);
        //code here
    }
};



//{ Driver Code Starts.

int main()
{   
    
    int t;
    
    //taking total testcases
    cin >> t;
    while(t--){
    string X, Y;
    //taking String X and Y
	cin >> X >> Y;
	
	//calling function shortestCommonSupersequence()
	Solution obj;
	cout << obj.shortestCommonSupersequence(X, Y, X.size(), Y.size())<< endl;
    }
	return 0;
}


// } Driver Code Ends