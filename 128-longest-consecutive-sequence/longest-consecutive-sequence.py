class Solution(object):
    def longestConsecutive(self,nums):
        nums = set(nums)
        nums = sorted(nums)
        nums = list(nums)
        high = [1]
        count=1
        if (len(nums)==0):
            return 0


        for i in range(0,len(nums)-1):
            if (nums[i]+1== nums[i+1]):
                count= count+1            
            else:
                high.append(count)
                count = 1
            if (i==len(nums)-2):
                high.append(count)
        
        high = set(high)
        high = sorted(high)
        
        return high[-1] 


        