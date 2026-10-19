class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        res=max(0,top-special[-1],special[0]-bottom)
        for i in range(len(special)-1):
            can=special[i+1]-special[i]-1
            res=max(res,can)
        return res

        