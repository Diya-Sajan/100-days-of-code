//{ Driver Code Starts
 
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	int len(string s){
	    int count = 0;
	    for(int i = 0; s[i]!='\0'; i++){
	        count++;
	    }
	    return count;
	}
	
	int isPalindrome(string s)
	{
	    int st = 0;
	    int e = len(s) -1;
	    while(st<e){
	        if(s[st]!=s[e]){
	            return false;
	        }
	        st++;
	        e--;
	    }
	    return true;
	}

};

//{ Driver Code Starts.

int main() 
{
   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s;
   		cin >> s;

   	    Solution ob;

   		cout << ob.isPalindrome(s) << "\n";
   	}

    return 0;
}
// } Driver Code Ends