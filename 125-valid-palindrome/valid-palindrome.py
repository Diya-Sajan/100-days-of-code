class Solution(object):
    def isPalindrome(self,s):
        s=s.lower()
        l=[]
        m=[]
        for i in s:
            if ((i>='a' and i<='z')):
                l.append(i)
            elif(i.isdigit()):
                l.append(int(i))
        for j in range(1, len(l)+1):
            m.append(l[-(j)])
            
        if (l==m):
            return True
        else: 
            return False