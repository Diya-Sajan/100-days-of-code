#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        f = {}
        for i in A:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        nf = sorted(f.items(), key=lambda x: x[1], reverse = True)
        if nf[0][1] > N/2:
            return nf[0][0]
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends