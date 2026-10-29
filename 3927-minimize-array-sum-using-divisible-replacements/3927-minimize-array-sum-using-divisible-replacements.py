class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        import math

        def divisors(x):
            res = []
            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    res.append(i)
                    if x//i != i:
                        res.append(x//i)
            return sorted(res)

        cnt = [0] * (max(nums) + 1)
        for e in nums:
            cnt[e] += 1

        res = 0
        for e in nums:
            for d in divisors(e):
                if cnt[d] > 0:
                    res += d
                    break

        return res