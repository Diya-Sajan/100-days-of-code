class Solution:
    def rotate(self, nums: List[int], l: int) -> None:
        lennn = len(nums)
        k = (len(nums)-l)%lennn
        nums[:]= nums[k:]+nums[:k]
        