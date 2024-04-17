//{ Driver Code Starts
// driver code

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution
{
  public:
    
    bool isPossible(int A[], int n, int k, long long mid){
        int P = 1;
        int curr_sum = 0;
        
        for(int i=0; i<n; i++){
            if(A[i]>mid){
                return false;
            }
            
            if(curr_sum+A[i]<=mid){
                curr_sum+=A[i];
            }
            else{
                P++;
                if(P>k){
                    return false;
                }
                curr_sum = A[i];
            }
        }
        return true;
    }
    
    long long minTime(int arr[], int n, int k)
    {
        long long s = 0;
        long long ans = -1;
        long long sum = 0;
        for(int i=0; i<n; i++){
            sum+=arr[i];
        }
        long long e = sum;
        long long mid = s + (e-s)/2;
        while(s<=e){
            if(isPossible(arr, n, k, mid)){
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

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int k,n;
		cin>>k>>n;
		
		int arr[n];
		for(int i=0;i<n;i++)
		    cin>>arr[i];
		Solution obj;
		cout << obj.minTime(arr, n, k) << endl;
	}
	return 0;
}
// } Driver Code Ends