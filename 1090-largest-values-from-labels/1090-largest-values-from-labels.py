class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        ar=[]
        d={}
        n=len(values)
        for i in range(n):
            ar.append((values[i],labels[i]))
            d[labels[i]]=0
        ar=sorted(ar,key=lambda x:-x[0])
        res=0
        for i in range(n):
            if numWanted != 0 and d[ar[i][1]]<useLimit:
                res+=ar[i][0]
                d[ar[i][1]]+=1
                numWanted-=1
        return res
