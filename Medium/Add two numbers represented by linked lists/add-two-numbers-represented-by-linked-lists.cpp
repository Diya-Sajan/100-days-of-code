//{ Driver Code Starts
// driver

#include <bits/stdc++.h>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

struct Node* buildList(int size)
{
    int val;
    cin>> val;
    
    Node* head = new Node(val);
    Node* tail = head;
    
    for(int i=0; i<size-1; i++)
    {
        cin>> val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    cout<< endl;
}


// } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    Node* reverse(Node* head){
        Node* prev=NULL;
        Node* curr=head;
        while(curr!=NULL){
            Node* forward=curr->next;
            curr->next=prev;
            prev=curr;
            curr=forward;
        }
        return prev;
    }
    Node* add(Node* first,Node* second){
        Node* ans=new Node(0);
        Node* temp=ans;
        int carry=0,sum=0;
        while(first!=NULL && second!=NULL){
            sum = carry+ first->data + second->data;
            carry=sum/10;
            int digit=sum%10;
            ans->next=new Node(digit);
            ans=ans->next;
            first=first->next;
            second=second->next;
        }
        while(first!=NULL){
            sum = carry+ first->data;
            carry=sum/10;
            int digit=sum%10;
            ans->next=new Node(digit);
            ans=ans->next;
            first=first->next;
        }
        while(second!=NULL){
            sum = carry+ second->data;
            carry=sum/10;
            int digit=sum%10;
            ans->next=new Node(digit);
            ans=ans->next;
            second=second->next;
        }
        if(carry!=0){
            ans->next=new Node(carry);
            ans=ans->next;
        }
        return temp->next;
    }
    //Function to add two numbers represented by linked list.
    struct Node* addTwoLists(struct Node* first, struct Node* second)
    {
        // first reverse both the linked list
        first=reverse(first);
        second=reverse(second);
        
        // this is the function for adding the digits
        Node* ans=add(first,second);
        // then reverse the ans linked list and return the head of the ans linked list
        ans=reverse(ans);
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
        int n, m;
        
        cin>>n;
        Node* first = buildList(n);
        
        cin>>m;
        Node* second = buildList(m);
        Solution ob;
        Node* res = ob.addTwoLists(first,second);
        printList(res);
    }
    return 0;
}

// } Driver Code Ends