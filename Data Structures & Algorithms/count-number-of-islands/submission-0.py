class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ): # out of bounds or 0
                return

            grid[r][c] = "0" # set all the connected 1's to 0, since we can only move by directions if the 1 is not reachable from this 1 then it's not in this island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": # already set other connected parts of the island to 0 so won't double count
                    dfs(r, c)
                    islands += 1

        return islands