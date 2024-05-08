#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        new=[]
        res = 0
        for i in range(n):
            new.append((arr[i],1))
            new.append((dep[i],-1))
        
        new = sorted(new, key=lambda x:x[1], reverse=True)
        new = sorted(new, key=lambda x:x[0])
        
        maxi=0
        for i in new:
            if i[1]==1:
                res+=1
            else:
                res-=1
            maxi = max(maxi,res)
        return maxi
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends