class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        d={}
        res=set()
        for j in range(len(nums)):
            need=nums[j]-k
            if need in d:
                res.add(nums[j])
            d[nums[j]]=1
        return len(res)
