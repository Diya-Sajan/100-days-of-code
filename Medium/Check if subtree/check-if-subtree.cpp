//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Tree Node
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to Build Tree
Node *buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
/* A binary tree node

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

class Solution
{ private:
   queue <Node*> req(Node* t, Node* s){
        queue<Node*> ans;
        queue< Node*> q;
        q.push(t);
        while (!q.empty()){
             Node* front=q.front();
             q.pop();
             if (front->data==s->data){
                 ans.push(front);
             }
             if (front->left){
                 q.push(front->left);
             }
             if (front->right){
                 q.push(front->right);
             }
        }
        return ans;
    }
    bool solve( Node* root, Node* s){
        if (root==NULL||s==NULL) return true;
        if (root->left&&s->left==NULL||!root->left&&s->left) return false;
        if (root->right&&s->right==NULL||!root->right&&s->right) return false;
        bool op1=solve(root->left,s->left);
        bool op2=solve(root->right,s->right);
        bool op3=false;
        if (root->data==s->data) op3=true;
        if (op1&&op2&&op3) return true;
        else return false;
    }
  public:
    //Function to check if S is a subtree of tree T.
    bool isSubTree(Node* t, Node* s) 
    {
        // Your code here
       queue< Node*> root=req(t,s);
       bool c=false;
       while (!root.empty()){
           Node* front=root.front();
           root.pop();
           c=solve(front,s);
           if (c==true) {
               break;
           }
       }
       return c;
    }
};


//{ Driver Code Starts.

int main() {
    int tc;
    scanf("%d ", &tc);
    while (tc--) {
        string strT, strS;
        getline(cin, strT);
        Node *rootT = buildTree(strT);
        getline(cin, strS);
        Solution obj;
        Node *rootS = buildTree(strS);
        cout << obj.isSubTree(rootT, rootS) << "\n";

    }
    return 0;
}
// } Driver Code Ends