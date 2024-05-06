//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution
{
    public:
    //Function to find the maximum occurring character in a string.
    char getMaxOccuringChar(string str)
    {
        // Your code here
        int a[26]={0};
        
        int n=str.length();
        for(int i=0; i<n; i++){
            if(str[i]>='a' && str[i]<='z'){
                int x = str[i]-'a';
                a[x]++;
            }
            if(str[i]>='A' && str[i]<='Z'){
                int y = str[i]-'A';
                a[y]++;
            }
        }
        int maxi = 0;
        for(int i=0; i<26; i++){
            //std::cout<<a[i]<<std::endl;
            if(a[i]>a[maxi]){
                maxi = i;
            }
        }
        return('a'+maxi);
    }

};

//{ Driver Code Starts.

int main()
{
   
    int t;
    cin >> t;
    while(t--)
    {
        string str;
        cin >> str;
    	Solution obj;
        cout<< obj.getMaxOccuringChar(str)<<endl;
    }
}
// } Driver Code Ends