class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res=0
        for d in range(1,a+1):
            if a%d==0 and b%d==0:
                res+=1
        return res