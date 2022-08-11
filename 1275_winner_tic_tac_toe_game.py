from typing import List


class UglySolution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        paper = [[0] * 3 for _ in range(3)]
        turn_A = True
        for row, col in moves:
            paper[row][col] = 1 if turn_A else -1
            turn_A = not turn_A
        for i in range(3):
            if sum(paper[i]) == 3 or paper[0][i] + paper[1][i] + paper[2][i] == 3:
                return 'A'
            if sum(paper[i]) == -3 or paper[0][i] + paper[1][i] + paper[2][i] == -3:
                return 'B'
        if paper[0][0] + paper[1][1] + paper[2][2] == 3 or \
            paper[0][2] + paper[1][1] + paper[2][0] == 3:
            return 'A'
        if paper[0][0] + paper[1][1] + paper[2][2] == -3 or \
            paper[0][2] + paper[1][1] + paper[2][0] == -3:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'


class NeatSolution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        paper = [[0] * 3 for _ in range(3)]
        # save moves in the paper array
        turn_A = True
        for row, col in moves:
            paper[row][col] = 1 if turn_A else -1
            turn_A = not turn_A
        win_condition = {3: 'A', -3: 'B'}
        for i in range(3):
            # check row_sum and col_sum
            for _sum in (sum(paper[i]), paper[0][i] + paper[1][i] + paper[2][i]):
                if _sum in win_condition:
                    return win_condition[_sum]
        # check diag_sum and reverse diag_sum
        for _sum in (paper[0][0] + paper[1][1] + paper[2][2], paper[0][2] + paper[1][1] + paper[2][0]):
            if _sum in win_condition:
                return win_condition[_sum]
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'

