//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/*
The structure of the class is as follows
class _stack{
stack<int> s;
int minEle;
public :
    int getMin();
    int pop();
    void push(int);
};
*/

class Solution{
    stack<pair<int,int>> s;
    public:
    
       /*returns min element from stack*/
       int getMin(){
           
           return s.size()==0?-1:s.top().second;
       }
       
       /*returns poped element from stack*/
       int pop(){
           
           if(s.size()==0){
               return -1;
           }
           int val = s.top().first;
           s.pop();
           return val;
       }
     
       /*push element x into the stack*/
       void push(int x){
           
           if(s.size()==0){
               s.push({x,x});
           }else{
               int minEle = min(s.top().second,x);
               s.push({x,minEle});
           }
       }
};

//{ Driver Code Starts.

int main()
 {
    long long t;

    cin>>t;
    while(t--)
    {
        int q;
        cin>>q;
        Solution ob;
        while(q--){
           int qt;
           cin>>qt;
           if(qt==1)
           {
              //push
              int att;
              cin>>att;
              ob.push(att);
           }
           else if(qt==2)
           {
              //pop
              cout<<ob.pop()<<" ";
           }
           else if(qt==3)
           {
              //getMin
              cout<<ob.getMin()<<" ";
           }
       }
       cout<<endl;
    }
    return 0;
}

// } Driver Code Ends