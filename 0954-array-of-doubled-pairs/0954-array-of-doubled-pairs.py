class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        arr.sort(key=lambda x:abs(x))
        n=len(arr)//2
        d={}
        for i in range(2*n):
            d[arr[i]]=d.get(arr[i],0)+1
        for e in arr:
            if d[e]==0:
                continue
            if 2*e not in d:
                return False
            d[e]-=1
            d[2*e]-=1
        for e in d:
            if d[e]!=0:
                return False
        return True