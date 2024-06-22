import re

class Solution:
    def ExtractNumber(self,sentence):
        sen = sentence.split(" ")
        ans = []
        for i in sen:
            if bool(re.search(r'\d', i)):
                if '9' not in i:
                    ans.append(int(i))
        if ans == []:
            return -1
        else:
            return max(ans)



#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends