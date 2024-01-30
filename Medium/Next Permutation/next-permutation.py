#User function Template for python3

class Solution:
    def nextPermutation(self,n,nums):
        #n=len(nums)
        #size of the array
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        #if the array is the max permutation itself return the sorted order
        if index==-1:
            nums.reverse()
            return nums
        else:    
            # Step 2: Find the next greater element and swap
            for i in range(n-1,index,-1):
                if nums[i]>nums[index]:
                    nums[i],nums[index]=nums[index],nums[i]
                    break
            #sort the remaining array after the index i.e reverse
            s=index+1
            e=n-1
            while s<=e:
                nums[s],nums[e]=nums[e],nums[s]
                s+=1
                e-=1
            return nums

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends