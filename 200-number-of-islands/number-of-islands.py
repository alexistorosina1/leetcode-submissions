class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isBound(grid, r, c):
            if r < 0 or c < 0:
                return False
            if r >= len(grid) or c >= len(grid[0]):
                return False
            return True

        def isWater(grid, r, c):
            if not isBound(grid, r, c):
                return True
            if grid[r][c] == "0":
                return True
            return False

        def dfs(grid, r,c):
            if (isWater(grid, r, c)):
                return
            grid[r][c] = "0"
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        land = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not (isWater(grid, r,c)):
                    land += 1
                    dfs(grid, r, c)
        return land
        # isWater(r, c)
        #       return grid[r][c] == 0

        # isBoundd(r,c)
        #       if r < numRows and c < numCols
        #       r >= 0 and c >= 0
    
        # dfs(r, c)
        #.    isBound r, c, not isWater
        #       destroy r,c -> grid[r][c] = 0
        #       dfs() ->up, dowm, left, right

        # iterate grid
        #  if land then num += 1, dfs
        # 


