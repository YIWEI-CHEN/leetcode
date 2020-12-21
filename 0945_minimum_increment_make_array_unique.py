import collections
from typing import List


class OOTSolution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # out of time
        h = {}
        moves = 0
        def find(num):
            while num in h:
                num = h[num] + 1
            h[num] = num
            return num
        for num in A:
            moves += find(num) - num
        return moves


class SortedSolution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        need, moves = 0, 0
        for num in A:
            moves += max(need - num, 0)
            need = max(need, num) + 1
        return moves


class FreqSolution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        moves = 0
        need = 0
        freq = collections.OrderedDict(sorted(collections.Counter(A).items()))
        for num, appearance in freq.items():
            moves += appearance * max(need - num, 0) + appearance * (appearance - 1) // 2
            need = max(need, num) + appearance
        return moves
