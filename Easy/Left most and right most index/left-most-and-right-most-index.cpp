//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
    long long firstOc(vector<long long> v, long long x){
        long long s = 0;
        long long e = v.size() - 1;
        long long mid = s + (e - s)/2;
        long long ans = -1;
        while(s<=e){
            
            if (v[mid] == x){
                ans = mid;
                e = mid - 1;
            }
            else if(x > v[mid]){
                s = mid + 1;
            }
            else if(x < v[mid]){
                e = mid - 1;
            }
            
            mid = s + (e-s)/2;
            
        }
        return ans;
    }
    
    long long lastOc(vector<long long> v, long long x){
        long long s = 0;
        long long e = v.size() - 1;
        long long mid = s + (e - s)/2;
        long long ans = -1;
        while(s<=e){
            
            if (v[mid] == x){
                ans = mid;
                s = mid + 1;
            }
            else if(x > v[mid]){
                s = mid + 1;
            }
            else if(x < v[mid]){
                e = mid - 1;
            }
            
            mid = s + (e-s)/2;
            
        }
        return ans;
    }
    
    pair<long,long> indexes(vector<long long> v, long long x)
    {
        pair<long long, long long> p;
        p.first = firstOc(v,x);
        p.second = lastOc(v,x);
        
        return p;
    }
};

//{ Driver Code Starts.

int main()
 {
    long long t;
    cin>>t;
    while(t--)
    {
        long long n, k;
        vector<long long>v;
        cin>>n;
        for(long long i=0;i<n;i++)
        {
            cin>>k;
            v.push_back(k);
        }
        long long x;
        cin>>x;
        Solution obj;
        pair<long,long> pair = obj.indexes(v, x);
        
        if(pair.first==pair.second and pair.first==-1)
        cout<< -1 <<endl;
        else
        cout<<pair.first<<" "<<pair.second<<endl;

    }
	return 0;
}

// } Driver Code Ends