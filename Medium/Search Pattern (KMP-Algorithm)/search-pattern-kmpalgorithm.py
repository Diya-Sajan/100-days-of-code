#User function Template for python3

class Solution:
    def search(self, pat, txt):
        
        lp = len(pat)
        lx = len(txt) 
        liss=[]
        
        for i in range(lx+1 - lp): 

            if txt[i]==pat[0]:

                if txt[i:i+lp]==pat:
                    
                    liss.append(i+1)
                
        if liss==[]:
            return [-1]
        else:
            return liss    
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends