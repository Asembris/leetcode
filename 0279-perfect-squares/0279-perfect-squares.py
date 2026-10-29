class Solution:
    def numSquares(self, n: int) -> int:
        import math
        def sqrt(x):
            if x<=0:
                return False
            d=int(math.sqrt(x))
            return d*d==x
        
        if sqrt(n):
            return 1 
        for a in range(1,n//2+1):
            if sqrt(n-a) and sqrt(a):
                return 2
        for c in range(1,int(math.sqrt(n))+1):
            for b in range(c,int(math.sqrt(n))+1):
                if sqrt(n-b*b-c*c):
                    return 3
        return 4
        