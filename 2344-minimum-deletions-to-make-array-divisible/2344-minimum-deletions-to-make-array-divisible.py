class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        from math import gcd
        g=0
        for e in numsDivide:
            g=gcd(e,g)
        nums=sorted(nums)
        for i in range(len(nums)):
            if g%nums[i]==0:
                return i
        return -1
            