"""
/////////////////
Number Of Islands
/////////////////

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000

Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3

Difficulty: MEDIUM
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "2"
                    island = []
                    island.append([i, j])
                    while island != []:
                        x = island[0][0]
                        y = island[0][1]
                        del island[0]
                        if x > 0 and grid[x-1][y] == "1":
                            grid[x-1][y] = "2"
                            island.append([x-1, y])
                        if y > 0 and grid[x][y-1] == "1":
                            grid[x][y-1] = "2"
                            island.append([x, y-1])
                        if x < len(grid)-1 and grid[x+1][y] == "1":
                            grid[x+1][y] = "2"
                            island.append([x+1, y])
                        if y < len(grid[x])-1 and grid[x][y+1] == "1":
                            grid[x][y+1] = "2"
                            island.append([x, y+1])
                j += 1
            i += 1
        return count
