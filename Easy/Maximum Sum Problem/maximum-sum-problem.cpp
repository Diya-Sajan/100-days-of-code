//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution
{
    public:
    int maxSum(int n)
    {
        vector<int> pre(n+1,0);
        for(int i=0;i<=n;i++)
        {
            int sum=pre[i/2]+pre[i/3]+pre[i/4];
            if(sum>=i)
            pre[i]=sum;
            else
            pre[i]=i;
        }
        return pre[n];
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
        cout<<ob.maxSum(n)<<"\n";
    }
    return 0;
}
// } Driver Code Ends