class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        d={0:1}
        res=0
        for j in range(1,n+1):
            need=pref[j]-k
            res+=d.get(need,0)                  
            d[pref[j]]=d.get(pref[j],0)+1
        return res
        