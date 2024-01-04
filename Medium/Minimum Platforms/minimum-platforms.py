#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        platforms = 0
        maxplatforms = 0
        vals = []
        for i in range(n):
            vals.append((arr[i],1))
            vals.append((dep[i],-1))


        vals = sorted(vals, key=lambda x:x[1], reverse=True)
        vals = sorted(vals, key=lambda x:x[0])
        for i in vals:
            #print(i, end = ' ')
            if i[1] == 1:
                platforms += 1
            elif i[1] == -1:
                platforms -= 1
                
            maxplatforms = max(platforms, maxplatforms)
        
        return maxplatforms
            
            

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