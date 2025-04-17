class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # i = i % n
        # if i == 0:
        #     return
        
        # flag = nums[-k:]
        k = k % len(nums)
        if k == 0:
            return
        
        nums[:]=nums[-k:]+nums[:-k]