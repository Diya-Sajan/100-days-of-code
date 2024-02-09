#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, nums, target):
        # Get the length of the input array
        n = len(nums)
        
        # If the array has less than 4 elements, return an empty list
        if n < 4:
            return []
        
        # Sort the input array
        nums.sort()
        
        # Initialize a set to store unique quadruplets that sum up to the target
        result = set()
        
        # Iterate through the array to find quadruplets
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    # Calculate the current sum of elements at indices i, j, left, and right
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        # If the sum is equal to the target, add the quadruplet to the result set
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left, right = left + 1, right - 1
                    elif current_sum < target:
                        # If the sum is less than the target, move the left pointer to the right
                        left += 1
                    else:
                        # If the sum is greater than the target, move the right pointer to the left
                        right -= 1
        
        # Convert the set of quadruplets to a sorted list
        return sorted(result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends