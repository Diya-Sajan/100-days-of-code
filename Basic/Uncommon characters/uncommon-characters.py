#User function Template for python3

class Solution:
    def UncommonChars(self, A, B):

        a = [*A]
        b = [*B]
        c = sorted(list(set(a+b)))
        newc = []
        for i in c:
            if not ((i in a) and (i in b)):
                newc.append(i)
        res = "".join(newc)
        if res == '': return -1
        else: return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends