//{ Driver Code Starts
// Program to find the maximum profit job sequence from a given array 
// of jobs with deadlines and profits 
#include<bits/stdc++.h>
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
}; 


// } Driver Code Ends
/*
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
};
*/

class Solution 
{
    public:
    //Function to find the maximum profit and the number of jobs done.
    static bool mycmp(const Job & j1 , const Job & j2  ){
        return j1.profit > j2.profit;
    }
    
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        // your code here
        // sort on the basis of profit 
        sort(arr,arr + n,mycmp);
        int maxdeadline = arr[0].dead;
        for(int i = 1; i<n ; i++){
            maxdeadline = max(maxdeadline,arr[i].dead);
        }
        vector<int>avail(maxdeadline+1,0);
        int total_profit = arr[0].profit;
        int number_of_jobs = 1;
        avail[arr[0].dead] = arr[0].id;
        for(int i = 1; i<n ;i++){
            int j = arr[i].dead;
            while(j>=1 and avail[j]!=0){
                j--;
            }
            if(j!=0){
                avail[j] = arr[i].id;
                total_profit += arr[i].profit;
                number_of_jobs++;
            }
        }
        return {number_of_jobs,total_profit};
        
    } 
};

//{ Driver Code Starts.
// Driver program to test methods 
int main() 
{ 
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        Job arr[n];
        
        //adding id, deadline, profit
        for(int i = 0;i<n;i++){
                int x, y, z;
                cin >> x >> y >> z;
                arr[i].id = x;
                arr[i].dead = y;
                arr[i].profit = z;
        }
        Solution ob;
        //function call
        vector<int> ans = ob.JobScheduling(arr, n);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
	return 0; 
}



// } Driver Code Ends