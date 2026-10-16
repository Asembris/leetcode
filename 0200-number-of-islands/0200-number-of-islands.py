from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m, res = len(grid), len(grid[0]), 0
        vis = {}

        def ver(x, y):
            return 0 <= x < n and 0 <= y < m
        
        def dfs(i, j):
            vis[(i, j)] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if ver(nx, ny) and (nx, ny) not in vis and grid[nx][ny] == '1':
                    dfs(nx, ny)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in vis:
                    dfs(i, j)
                    res += 1
        return res