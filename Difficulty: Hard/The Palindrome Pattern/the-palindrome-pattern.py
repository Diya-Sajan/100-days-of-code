#User function Template for python3

def pal(ar):
    if ar[:]==ar[::-1]:
        return True
    else: return False
class Solution:
        
    def pattern (self, arr):
        n = len(arr)
        m = len(arr[0])
        for i in range(n):
            if(pal(arr[i])):
                return str(i)+" R"
        for i in range(n):
            ar = []
            for j in range(n):
                ar.append(arr[j][i])
            if(pal(ar)):
                return str(i)+" C"
                
        return "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends