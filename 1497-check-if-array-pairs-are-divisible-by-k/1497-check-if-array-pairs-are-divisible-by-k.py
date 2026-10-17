class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        if k==1:
            return True
        mod=[0]*k
        for e in arr:
            mod[e%k]+=1
        if mod[0]%2!=0:
            return False
        for i in range(k):
            if mod[i]!=mod[(k-i)%k]:
                return False
        return True