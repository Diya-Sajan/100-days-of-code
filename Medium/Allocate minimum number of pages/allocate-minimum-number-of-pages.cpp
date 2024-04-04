//{ Driver Code Starts
// Initial template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template in C++

class Solution 
{
    public:
    bool isPossible(int A[], int n, int m, int mid){
        int studentsReq = 1;
        int curr_sum = 0;
        
        for(int i=0; i<n; i++){
            if(A[i]>mid){
                return false;
            }
            
            if(curr_sum+A[i]<=mid){
                curr_sum+=A[i];
            }
            else{
                studentsReq++;
                if(studentsReq>m){
                    return false;
                }
                curr_sum = A[i];
            }
        }
        return true;
    }
    //Function to find minimum number of pages.
    int findPages(int A[], int n, int m) 
    {
        if(n<m){
            return -1;
        }
        int s = 0;
        int ans = -1;
        int sum = 0;
        for(int i=0; i<n; i++){
            sum+=A[i];
        }
        int e = sum;
        int mid = s + (e-s)/2;
        while(s<=e){
            if(isPossible(A,n,m,mid)){
                ans = mid;
                e = mid - 1;
            }
            else{
                s = mid + 1;
            }
            mid = s + (e-s)/2;
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int A[n];
        for(int i=0;i<n;i++){
            cin>>A[i];
        }
        int m;
        cin>>m;
        Solution ob;
        cout << ob.findPages(A, n, m) << endl;
    }
    return 0;
}

// } Driver Code Ends