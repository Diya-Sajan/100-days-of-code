#User function template for Python 3

class Solution:
    def majorityElement(self, arr, N):
        '''
        f = {}
        for i in A:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        nf = sorted(f.items(), key=lambda x: x[1], reverse = True)
        if nf[0][1] > int(N/2):
            return nf[0][0]
        return -1
        '''
        el = -1
        votes = 0
        for i in range (N):
            if (votes == 0):
                el = arr[i]
                votes = 1
            else:
                if (arr[i] == el):
                    votes += 1
                else:
                    votes -= 1
        count = 0
        
        for i in range (N):
            if (arr[i] == el):
                count += 1
                 
        if (count > N // 2):
            return el
        else:
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