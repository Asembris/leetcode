class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        res=0
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            res+=(j-i-1)
            i=j
        return res