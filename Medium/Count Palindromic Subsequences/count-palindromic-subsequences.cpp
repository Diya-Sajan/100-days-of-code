//{ Driver Code Starts
// Counts Palindromic Subsequence in a given String
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
    public:
    
    typedef long long int ll;
    const int mod = 1e9+7;
    
    long long int  countPS(string str)
    {
        ll n = str.length();
        
        vector<vector<ll>>dp(n+1,vector<ll>(n+1));
        
        // dp[i][j] --> No.of Palindromic subsequences from [i....j]
        
        
        // Length of Suseq.  ==> 1 
        
        for(ll i=1;i<=n;i++){
            dp[i][i]=1; 
        }
        
        // Length 2 
        // 'aa' => a,a,aa => 3 ,,, 
        // 'ab' => a,b => 2
        
        for(ll i=1;i<n;i++){ // n
            if(str[i-1]==str[i]){
                dp[i][i+1]=3;
            }
            else{
                dp[i][i+1]=2;
            }
        }
        
        // Length 3 
        
        /* Case 1) Start and End character same */
        // 'aaa' ,  => 'aaa', a,a,a,aa,aa,aaa
        // dp[1][3] = dp[1][2] + dp[2][3] - dp[2][2] + dp[2][2] + 1
        
        /* Case 2) Start and End character not same */
        // 'abb', =? a,b,b,bb
        // dp[1][3]= dp[1][2] + dp[2][3] - dp[2][2]
        
        ll len=3;
        while(len<=n){
            ll i=1;
            
            while(i<=(n-len+1)){
                ll j = i+len-1;
                
                if(str[i-1]==str[j-1]){
                    dp[i][j]=dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1]+dp[i+1][j-1]+1;
                    // dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1] => This is Already Present
                    //  dp[i+1][j-1] => That many produce,, same character at start and end. e.b : 'xabx'
                    // + 1 => 'xx' as one new palindrome subsequence
                }
                else{
                    dp[i][j]=dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1];
                }
                dp[i][j]=dp[i][j]%mod;
                i++;
            }
            len++;
        }
        return (dp[1][n]+mod)%mod;
    }
     
};


//{ Driver Code Starts.
// Driver program
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string str;
        cin>>str;
        Solution ob;
        long long int ans = ob.countPS(str);
        cout<<ans<<endl;
    } 
}
// } Driver Code Ends