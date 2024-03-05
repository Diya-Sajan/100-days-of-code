//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int solve(int b,int e,int *arr,vector<vector<int>> &dp){
        if(e-b==1) return 0;
        else if(dp[b][e]!=-1) return dp[b][e];
        int p=INT_MAX;
        for(int k=b+1;k<e;k++){
            int ls=solve(b,k,arr,dp);
            int rs=solve(k,e,arr,dp);
            p=min(p,ls+rs+(arr[b]*arr[k]*arr[e]));
        }
        return dp[b][e]=p;
    }
    int matrixMultiplication(int N, int arr[])
    {
        vector<vector<int>> dp(N,vector<int>(N,0));

//solve(0,N-1,arr,dp);//for memoization

//tabulation:

        for(int i=N-1;i>=0;i--){
            for(int j=i+1;j<N;j++){
                if(j-i<2) continue;
                int p=INT_MAX;
                for(int k=i+1;k<j;k++){
                    int ls=dp[i][k];
                    int rs=dp[k][j];
                    p=min(p,ls+rs+(arr[i]*arr[k]*arr[j]));
                }
                dp[i][j]=p;
            }
        }
        return dp[0][N-1];
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[N];
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        Solution ob;
        cout<<ob.matrixMultiplication(N, arr)<<endl;
    }
    return 0;
}
// } Driver Code Ends