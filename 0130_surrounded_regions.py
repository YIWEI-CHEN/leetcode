from typing import List


class DFSSolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        if num_rows == 0:
            return
        num_cols = len(board[0])
        visited = [[False] * num_cols for _ in range(num_rows)]  # [[False] * num_cols] * num_row will cause unexpected memory sharing

        def reverse_max_region(row, col):
            stack = [(row, col)]
            reverse_candidates = []
            reverse = True
            while stack:
                row, col = stack.pop()
                if board[row][col] == 'O':
                    visited[row][col] = True
                    reverse_candidates.append((row, col))
                    if row in [0, num_rows - 1] or col in [0, num_cols - 1]:
                        reverse = False
                left, right = col - 1, col + 1
                up, down = row - 1, row + 1
                if right < num_cols and not visited[row][right] and board[row][right] == 'O':
                    stack.append((row, right))
                if down < num_rows and not visited[down][col] and board[down][col] == 'O':
                    stack.append((down, col))
                if left >= 0 and not visited[row][left] and board[row][left] == 'O':
                    stack.append((row, left))
                if up >= 0 and not visited[up][col] and board[up][col] == 'O':
                    stack.append((up, col))
            if reverse:
                for row, col in reverse_candidates:
                    board[row][col] = 'X'

        for row in range(num_rows):
            for col in range(num_cols):
                if visited[row][col] or board[row][col] == 'X':
                    continue
                reverse_max_region(row, col)


if __name__ == '__main__':
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # e = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    # board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    # e = [["O", "X", "X", "O", "X"], ["X", "X", "X", "X", "O"], ["X", "X", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
    # board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    # e = [["O","O","O"],["O","O","O"],["O","O","O"]]
    board = [["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"]]
    e = [["X","O","X","X"],["O","X","X","X"],["X","X","X","O"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]
    DFSSolution().solve(board)
    print(board)
    print(e == board)
