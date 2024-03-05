//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends

class Solution {
public:
    // Max heap to store the smaller half of the elements
    priority_queue<int> max_heap;
    // Min heap to store the larger half of the elements
    priority_queue<int, vector<int>, greater<int>> min_heap;

    // Function to insert an element into the heaps
    void insertHeap(int &x) {
        // If the element is greater than or equal to the top of the max heap,
        // insert it into the min heap. Otherwise, insert it into the max heap.
        if (max_heap.size() && x >= max_heap.top())
            min_heap.push(x);
        else
            max_heap.push(x);
        
        // Ensure that the heaps are balanced
        balanceHeaps();
    }

    // Function to balance the sizes of the heaps
    void balanceHeaps() {
        if (abs(max_heap.size() - min_heap.size()) > 1) {
            // If the difference in sizes is greater than 1, rebalance the heaps
            if (max_heap.size() > min_heap.size()) {
                int temp = max_heap.top();
                max_heap.pop();
                min_heap.push(temp);
            } else {
                int temp = min_heap.top();
                min_heap.pop();
                max_heap.push(temp);
            }
        }
    }

    // Function to return the median
    double getMedian() {
        double ans = 0.0;
        int total = max_heap.size() + min_heap.size();
        // If the total number of elements is odd, return the middle element
        if (total & 1) {
            if (max_heap.size() > min_heap.size())
                ans += max_heap.top();
            else
                ans += min_heap.top();
        } 
        // If the total number of elements is even, return the average of the two middle elements
        else {
            if (max_heap.size()) ans += max_heap.top();
            if (min_heap.size()) ans += min_heap.top();
            ans = ans / 2.0;
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main()
{
    int n, x;
    int t;
    cin>>t;
    while(t--)
    {
    	Solution ob;
    	cin >> n;
    	for(int i = 1;i<= n; ++i)
    	{
    		cin >> x;
    		ob.insertHeap(x);
    	    cout << floor(ob.getMedian()) << endl;
    	}
    }
	return 0;
}
// } Driver Code Ends