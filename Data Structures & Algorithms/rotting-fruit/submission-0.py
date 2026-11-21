class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visit = set()
        fresh = 0

        def dfs(i, j):
            nonlocal fresh
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or (i,j) in visit:
                return
            else:
                visit.add((i,j))
                q.append([i,j])
                grid[i][j] = 2
                fresh -= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visit.add((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minute = 0
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
            minute += 1

        return minute if fresh == 0 else -1


