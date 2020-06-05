import random
from typing import List


class WrongSolution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sums = [0]  # wrong
        prefix_sum = 0
        for w_ in w:
            prefix_sum += w_
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        v = random.random() * self.total_sum
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = int((low + high) / 2)
            if v > self.prefix_sums[mid]:
                low = mid  # wrong
            else:
                high = mid
        return low


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sums = []
        prefix_sum = 0
        for w_ in w:
            prefix_sum += w_
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        v = random.random() * self.total_sum
        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = low + (high - low) // 2
            # mid = (low + high) // 2
            if v > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    w = [1, 2, 1]
    s = Solution(w)
    idx = s.pickIndex()
    print(idx)