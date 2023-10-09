class Solution(object):
    def containsDuplicate(self,nums):

        a = len(nums)
        nums = set(nums)
        nums = list(nums)
        b = len(nums)
        if (a!=b):
            return True
        elif(a==b):
            return False
        