#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        
        curr1 , curr2 = num1 , num2 
        
        res1 , res2 = "" , ""
        while curr1:
            res1+=str(curr1.data)
            curr1 = curr1.next 
        while curr2:
            res2+=str(curr2.data)
            curr2 = curr2.next 
        
        
        res1 , res2  = res1 , res2
        
        res1 , res2 = int(res1) , int(res2)
        
        res = res1 + res2
        
        res = str(res)[::-1]
        
        
        head = None
        
        for i in res:
            new_node = Node(i)
            new_node.next = head
            head = new_node
            
        return head
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)
        
        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
# } Driver Code Ends