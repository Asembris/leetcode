class Solution:
    def findGCD(self, nums: list[int]) -> int:
        import math
        nums.sort()
        g=math.gcd(nums[0],nums[-1])
        return g