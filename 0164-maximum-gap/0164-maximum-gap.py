class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        res=0
        nums.sort()
        for i in range(len(nums)-1):
            res=max(res,nums[i+1]-nums[i])
        return res
        