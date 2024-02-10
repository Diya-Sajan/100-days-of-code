//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
public:
    vector<int> maxMeetings(int n, vector<int>& s, vector<int>& f) {
        vector<vector<int>> temp;
        for (int i = 0; i < n; ++i) {
            temp.push_back({s[i], f[i], i + 1});
        }

        sort(temp.begin(), temp.end(), [](const vector<int>& a, const vector<int>& b) {
            return (a[1] == b[1]) ? a[2] < b[2] : a[1] < b[1];
        });

        vector<int> res = {temp[0][2]};

        for (int i = 1; i < n; ++i) {
            if (temp[i][0] > f[res.back() - 1]) {
                res.push_back(temp[i][2]);
            }
        }

        sort(res.begin(), res.end());

        return res;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> S(n),F(n);
        for(int i=0;i<n;i++){
            cin>>S[i];
        }
        for(int i=0;i<n;i++){
            cin>>F[i];
        }
        Solution ob;
        vector<int> ans=ob.maxMeetings(n,S,F);
        for(int i=0;i<ans.size();i++){
            cout<<ans[i];
            if(i!=ans.size()-1){
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends