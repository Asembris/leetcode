class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:

        co = [p1, p2, p3, p4]

        def dist(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        d = sorted(dist(co[i], co[j])
                   for i in range(4)
                   for j in range(i+1, 4))

        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5] == 2*d[0]
        