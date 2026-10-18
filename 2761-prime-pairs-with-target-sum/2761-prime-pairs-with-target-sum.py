class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        pr=[True]*(n+1)
        res=[]
        pr[1]=False
        i=2
        while i*i <=n:
            if pr[i]:
                j=i*i
                while j<=n:
                    pr[j]=False
                    j+=i
            i+=1
        for x in range(2,n//2+1):
            if pr[x] and pr[n-x]:
                res.append((x,n-x))
        res=sorted(res,key=lambda x:x[0])
        return res