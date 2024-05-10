#User function Template for python3

class Solution:
    def maxSubarrayXOR(self, N, arr):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.value = None
                
        def insert(root, num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
            node.value = num

        def findMaxXOR(root, nums):
            max_xor = float('-inf')
            for num in nums:
                curr_xor = 0
                node = root
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit ^ 1 in node.children:
                        node = node.children[bit ^ 1]
                        curr_xor |= 1 << i
                    else:
                        node = node.children[bit]
                max_xor = max(max_xor, curr_xor)
            return max_xor

        root = TrieNode()
        insert(root, 0)
        prefix_xor = 0
        max_xor = float('-inf')
        for num in arr:
            prefix_xor ^= num
            insert(root, prefix_xor)
            max_xor = max(max_xor, findMaxXOR(root, [prefix_xor]))
        return max_xor
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.maxSubarrayXOR(N,arr))
        

# } Driver Code Ends