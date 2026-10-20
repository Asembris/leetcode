class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        pr = [True] * (right + 1)
        pr[0] = False
        pr[1] = False
        i = 2
        while i * i <= right:
            if pr[i]:
                for j in range(i * i, right + 1, i):
                    pr[j] = False
            i += 1
        score=float("inf")
        res=[-1,-1]
        val=[]
        for x in range(left,right+1):
            if pr[x]:
                val.append(x)
        for i in range(len(val)-1):
            cur=val[i+1]-val[i]
            if cur<score or (cur == score and res[0]>val[i]):
                score=cur
                res=[val[i],val[i+1]]
        return res
