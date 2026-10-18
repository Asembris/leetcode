class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        from math import sqrt
        div=[]
        for d in range(1,int(sqrt(n))+1):
            if n%d==0:
                div.append(d)
                if n//d!=d:
                    div.append(n//d)
        div.sort()
        res=-1 if k>len(div) else div[k-1]
        return res