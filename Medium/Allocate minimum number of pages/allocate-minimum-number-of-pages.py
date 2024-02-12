class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        beg = max(A)
        end = sum(A) 
        ans =  0 
        while beg <= end:
            mid  = (beg + end) // 2
            # distribution
            c = 1
            p =  0
            for i in range(N):
                p  += A[i]
                if p  > mid:
                    c +=1
                    p = A[i]
                    # break
            if c <= M:
                # for checking the diffrences betweeen the students
                ans = mid 
                end  = mid - 1
            else:
                beg = mid + 1
        if M > N:
            return -1
        else:
            
            return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends