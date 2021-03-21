import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        if num_rows == 0:
            return 0
        num_cols = len(grid[0])
        visited = [[False] * num_cols for _ in range(num_rows)]

        def reverse_max_region(row, col):
            queue = collections.deque([(row, col)])
            while queue:
                x, y = queue.popleft()
                if x < 0 or x >= num_rows or y < 0 or y >= num_cols or visited[x][y]:
                    continue
                visited[x][y] = True
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    top, down = x - 1, x + 1
                    left, right = y - 1, y + 1
                    queue.append((x, left))
                    queue.append((x, right))
                    queue.append((top, y))
                    queue.append((down, y))

        num_island = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '0':
                    continue
                else:
                    reverse_max_region(row, col)
                    num_island += 1
        return num_island


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    expected = 1
    ans = Solution().numIslands(grid)
    print(ans == expected)
