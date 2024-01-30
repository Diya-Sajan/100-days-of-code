#User function Template for python3

class Solution:
    def findSubArrays(self,arr,n):
        cnt = 0
        sum_dict = {0:1}
        prev_sum = 0
        
        for ele in arr:
            prev_sum += ele
        
            if prev_sum in sum_dict:
                cnt += sum_dict[prev_sum]
            
            sum_dict[prev_sum] = sum_dict.get(prev_sum,0)+1
        
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends