#User function Template for python3

class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        m1,m2,c1,c2=None,None,None,None
        try:
            m1=(q1[1]-p1[1])/(q1[0]-p1[0])
            c1=p1[1]-(p1[0]*m1)
        except:
            m1=float("inf")
        try:
            m2=(q2[1]-p2[1])/(q2[0]-p2[0])
            c2=p2[1]-(p2[0]*m2)
        except:
            m2=float("inf")
        if m1==float("inf"):
            yInter=m2*p1[0]+c2
            if min(p1[1],q1[1])<=yInter<=max(p1[1],q1[1]):
                return "true"
            return "false"
        if m2==float("inf"):
            yInter=m1*p2[0]+c1
            if min(p2[1],q2[1])<=yInter<=max(p2[1],q2[1]):
                return "true"
            return "false"
        if m1==m2:
            if c1==c2:
                return "true"
            return "false"
        else:
            xInter=-(c1-c2)/(m1-m2)
            if min(p1[0],q1[0])<=xInter<=max(p1[0],q1[0]) and min(p2[0],q2[0])<=xInter<=max(p2[0],q2[0]):
                return "true"
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)

# } Driver Code Ends