class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import deque


        indeg=[0]*numCourses
        g=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            g[y].append(x)
            indeg[x]+=1
        
        dq=deque()
        for i in range(numCourses):
            if indeg[i]==0:
                dq.append(i)
        while len(dq):
            s=dq.popleft()
            if indeg[s]!=0:
                break
            for e in g[s]:
                indeg[e]-=1
                if indeg[e]==0:
                    dq.append(e)
        return all(e==0 for e in indeg)

        


