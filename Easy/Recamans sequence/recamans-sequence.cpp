//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
    public:
    void help(int& n,int pre,int i,unordered_map<int,int>& mp,vector<int>& ans)
    {
        //base case
        if(i>n)
        return ;
        
        //recursive calls
        //and small calculation
        int curr=pre-i;
        if(curr<0 or mp.count(curr))
        curr+=(2*i);
        
        mp[curr]=1;
        ans.push_back(curr);
        
        help(n,curr,i+1,mp,ans);
    }
    vector<int> recamanSequence(int n){
        unordered_map<int,int> mp;
        vector<int> ans;
        int pre=0;
        mp[0]=1;
        ans.push_back(0);
        
        help(n,0,1,mp,ans);
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<int> ans = ob.recamanSequence(n);
        for(int i = 0;i < n;i++)
            cout<<ans[i]<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends