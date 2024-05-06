//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

using namespace std;
class Solution
{
    public:
    //Function to reverse words in a given string.
    string reverseWords(string s) 
    { 
        // code here 
        string res = "";
        string temp = "";
        int i = 0;
        while(i<=s.length()-1){
            temp=temp+s[i];
            char ss = s[i+1];
            if(ss=='.'){
                res.insert(0,temp);
                res.insert(0,".");
                temp = "";
                i++;
            }
            
            if(ss=='\0'){
                res.insert(0,temp);
                temp = "";
                i++;
            }
            
            i++;
        }
        return(res);
    } 
};

//{ Driver Code Starts.
int main() 
{
    int t;
    cin >> t;
    while (t--) 
    {
        string s;
        cin >> s;
        Solution obj;
        cout<<obj.reverseWords(s)<<endl;
    }
}
// } Driver Code Ends