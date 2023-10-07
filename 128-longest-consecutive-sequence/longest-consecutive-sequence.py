class Solution(object):
    def longestConsecutive(self,nums):
        if (len(nums)==0):
            return 0

        nums = sorted(set(nums))
        nums = list(nums)
                    
        high = [1]
        count=1
        
        for i in range(0,len(nums)-1):
            if (nums[i]+1== nums[i+1]):
                count= count+1            
            else:
                high.append(count)
                count = 1
            if (i==len(nums)-2):
                high.append(count)
        
        return max(high) 


        