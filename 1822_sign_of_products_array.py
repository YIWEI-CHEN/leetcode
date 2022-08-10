from typing import List


class MySolution:
    # Drawback: iterate nums twice
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        num_neg = sum([n < 0 for n in nums])
        if num_neg % 2 == 0:
            return 1
        else:
            return -1


class BetterSolution:
    # Drawback: iterate nums once
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign *= -1
        return sign

