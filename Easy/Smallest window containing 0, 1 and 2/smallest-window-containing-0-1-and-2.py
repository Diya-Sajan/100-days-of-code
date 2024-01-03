#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        n = len(s)
        
        pos1=-1
        pos2=-1
        pos0=-1
        
        lengprev = n
        
        for i in range(n):
            if s[i]=='0':
                pos0 = i
            elif s[i]=='1':
                pos1 = i
            elif s[i]=='2':
                pos2 = i
            
            if min(pos0,pos1,pos2) == -1:
                if i == (n-1):
                    return -1
                continue
            leng = 1 + (max(pos0,pos1,pos2) - min(pos0,pos1,pos2))
            
            if leng<lengprev:
                lengprev =leng
        
        return min(leng,lengprev)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends